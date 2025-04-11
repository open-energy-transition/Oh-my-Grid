from flask import Flask, request, Response
import requests
import re

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    query = request.args.get('data')
    if not query:
        return Response('Missing "data" query parameter', status=400)

    overpass_url = f'https://overpass-api.de/api/interpreter?data={query}'

    try:
        r = requests.get(overpass_url)
        r.raise_for_status()
        xml = r.text

        # Protect already-valid XML entities
        placeholder_map = {
            '&amp;': '___AMP___',
            '&lt;': '___LT___',
            '&gt;': '___GT___',
            '&quot;': '___QUOT___',
            '&apos;': '___APOS___',
            '&#': '___HASH___'  # numeric entities
        }
        for entity, placeholder in placeholder_map.items():
            xml = xml.replace(entity, placeholder)

        # Replace any remaining bare ampersands with &amp;
        xml = re.sub(r'&(?!\w+;)', '&amp;', xml)

        # Restore original valid entities
        for entity, placeholder in placeholder_map.items():
            xml = xml.replace(placeholder, entity)

        return Response(xml, content_type='text/xml')

    except requests.exceptions.RequestException as e:
        return Response(f'Error fetching Overpass data: {str(e)}', status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
