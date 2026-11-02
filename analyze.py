import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

client = ImageAnalysisClient(
    endpoint=os.environ["VISION_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["VISION_KEY"])
)

with open("page.jpeg", "rb") as f:
    result = client.analyze(
        image_data=f.read(),
        visual_features=[VisualFeatures.READ, VisualFeatures.TAGS]
    )

if result.caption:
    print(f"Caption: {result.caption.text} ({result.caption.confidence:.2f})")

print("\nExtracted text (OCR):")
if result.read:
    for block in result.read.blocks:
        for line in block.lines:
            print(line.text)

print("\nTags:")
for tag in result.tags.list:
    print(f"{tag.name}: {tag.confidence:.2f}")
