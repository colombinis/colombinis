import os
import re
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import time

def fetch_trends():
    pytrends = TrendReq(hl='es-AR', tz=180)
    keywords = [
        'PHP', 'Magento', 'React', 'Docker', 'Wordpress',
        'Nextjs', 'Vue', 'opencode', 'laravel', 'IA',
        'mage-os', 'marko'
    ]

    trends_report = []

    for kw in keywords:
        try:
            print(f"Fetching trends for: {kw}")
            pytrends.build_payload([kw], timeframe='now 7-d', geo='AR')
            related_queries = pytrends.related_queries()

            if kw in related_queries:
                rising = related_queries[kw]['rising']
                if rising is not None and not rising.empty:
                    # Tomar los 3 primeros en aumento
                    top_rising = rising.head(3)['query'].tolist()
                    trends_report.append(f"**{kw}**: " + ", ".join(top_rising))

            # Pequeña pausa para evitar rate limiting
            time.sleep(1)

        except Exception as e:
            print(f"Error fetching trends for {kw}: {e}")
            continue

    if not trends_report:
        return "No se encontraron tendencias significativas en la última semana para el stack tecnológico."

    return "\n".join([f"- {item}" for item in trends_report])

def update_readme(trends_content):
    readme_path = 'README.md'
    if not os.path.exists(readme_path):
        print("README.md not found")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Marcadores
    start_marker = "<!-- TRENDS_START -->"
    end_marker = "<!-- TRENDS_END -->"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_section = f"{start_marker}\n\n*Última actualización: {now} (Argentina)*\n\n{trends_content}\n\n{end_marker}"

    # Reemplazar el contenido entre los marcadores
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    updated_content = pattern.sub(new_section, content)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == "__main__":
    print("Iniciando actualización de tendencias...")
    trends = fetch_trends()
    update_readme(trends)
    print("Actualización completada.")
