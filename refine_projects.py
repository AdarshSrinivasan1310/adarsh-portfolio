import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project

# 1. Remove Ace Creatives
Project.objects.filter(title__icontains='Ace Creativess').delete()

# 2. Add Vision Identity if it doesn't exist
vision_identity_desc = "A biometric system focused on an AI-driven building workflow for identity verification using Python, with a structured app/database/model architecture."
Project.objects.get_or_create(
    title="VisionIdentity: AI-Driven Biometric Identity",
    defaults={
        "description": vision_identity_desc,
        "github_link": "https://github.com/AdarshSrinivasan1310/VisionIdentity"
    }
)

# 3. Update links for others
links_to_update = {
    'SpectrumSqueeze': 'https://github.com/AdarshSrinivasan1310/SpectrumSqueeze',
    'SentinelFlow': 'https://github.com/AdarshSrinivasan1310/SentinelFlow',
    'VisionCart': 'https://github.com/AdarshSrinivasan1310/VisionCart',
}

for title_part, url in links_to_update.items():
    project = Project.objects.filter(title__icontains=title_part).first()
    if project:
        project.github_link = url
        project.save()

print("Project database updated and URLs added!")
