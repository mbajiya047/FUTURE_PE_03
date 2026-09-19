import os
import json
import shutil

print("Reading source markdown and template files...")

base_dir = os.path.dirname(__file__)
outputs_dir = os.path.join(base_dir, "outputs")
config_dir = os.path.join(base_dir, "config")

with open(os.path.join(outputs_dir, "02_pillar_blog_full.md"), "r", encoding="utf-8") as f:
    pillar_md = f.read()

with open(os.path.join(outputs_dir, "03_supporting_blogs_pack.md"), "r", encoding="utf-8") as f:
    supporting_md = f.read()

with open(os.path.join(outputs_dir, "04_internal_linking_matrix.md"), "r", encoding="utf-8") as f:
    linking_md = f.read()

with open(os.path.join(outputs_dir, "05_local_seo_playbook.md"), "r", encoding="utf-8") as f:
    local_seo_md = f.read()

with open(os.path.join(config_dir, "brand_variables.json"), "r", encoding="utf-8") as f:
    brand_vars = json.load(f)

with open(os.path.join(base_dir, "template.html"), "r", encoding="utf-8") as f:
    template_html = f.read()

# Extract schema
schema_part = local_seo_md.split('```html')[1].split('```')[0].strip()

# Split supporting articles
art1_part = supporting_md.split("# ARTICLE 1:")[1].split("# ARTICLE 2:")[0]
art2_part = supporting_md.split("# ARTICLE 2:")[1].split("# ARTICLE 3:")[0]
art3_part = supporting_md.split("# ARTICLE 3:")[1].split("# ARTICLE 4:")[0]
art4_part = supporting_md.split("# ARTICLE 4:")[1]

art1_content = ("# ARTICLE 1:" + art1_part).strip()
art2_content = ("# ARTICLE 2:" + art2_part).strip()
art3_content = ("# ARTICLE 3:" + art3_part).strip()
art4_content = ("# ARTICLE 4:" + art4_part).strip()

print(f"Pillar length: {len(pillar_md)}, Art1: {len(art1_content)}, Art2: {len(art2_content)}, Art3: {len(art3_content)}, Art4: {len(art4_content)}")

# Build JavaScript initial data bundle
articles_data = [
    {
        "id": "art-pillar",
        "type": "pillar",
        "category": "Pillar Article",
        "title": "The Complete Guide to Dental Implants in Bangalore: Procedure, Costs, Recovery & Specialist Selection",
        "slug": "/dental-implants-bangalore",
        "primary_keyword": "dental implants in bangalore",
        "secondary_keywords": ["best dentist bangalore", "dental implant specialist indiranagar", "tooth replacement bangalore"],
        "search_intent": "Commercial / Local Transactional",
        "target_word_count": 2600,
        "content": pillar_md
    },
    {
        "id": "art-cost",
        "type": "supporting",
        "category": "Cost & Commercial",
        "title": "Dental Implant Cost in Bangalore (2026 Price Breakdown)",
        "slug": "/dental-implant-cost-bangalore",
        "primary_keyword": "dental implant cost bangalore",
        "secondary_keywords": ["single tooth implant cost bangalore", "full mouth dental implant cost bangalore", "all on 4 dental implant price bangalore"],
        "search_intent": "Commercial Investigation",
        "target_word_count": 1400,
        "content": art1_content
    },
    {
        "id": "art-timeline",
        "type": "supporting",
        "category": "Procedure & FAQ",
        "title": "How Long Do Dental Implants Really Take? Timeline & Procedure Stages",
        "slug": "/dental-implant-timeline-healing",
        "primary_keyword": "dental implant procedure timeline bangalore",
        "secondary_keywords": ["how long do dental implants take", "stages of dental implant healing", "same day dental implants bangalore"],
        "search_intent": "Informational",
        "target_word_count": 1250,
        "content": art2_content
    },
    {
        "id": "art-safety",
        "type": "supporting",
        "category": "Safety & Candidacy",
        "title": "Are Dental Implants Safe? Success Rates, Risks & Candidate Checklist",
        "slug": "/are-dental-implants-safe",
        "primary_keyword": "are dental implants safe",
        "secondary_keywords": ["dental implant success rate india", "dental implant failure signs", "dental implants for diabetic patients bangalore"],
        "search_intent": "Informational / Evaluation",
        "target_word_count": 1300,
        "content": art3_content
    },
    {
        "id": "art-aftercare",
        "type": "supporting",
        "category": "Aftercare & Recovery",
        "title": "Dental Implant Aftercare Guide: Diet, Oral Hygiene & Recovery",
        "slug": "/dental-implant-aftercare-guide",
        "primary_keyword": "dental implant aftercare instructions",
        "secondary_keywords": ["what to eat after dental implant surgery", "dental implant recovery tips", "how to clean dental implants"],
        "search_intent": "Informational / Post-Op",
        "target_word_count": 1150,
        "content": art4_content
    }
]

# Keywords dataset
keywords_data = [
    {"keyword": "dental implants in bangalore", "intent": "Commercial", "location": "Bangalore Urban", "priority": "High", "contentType": "Pillar Blog", "targetPage": "/dental-implants-bangalore", "cpc": "₹92.50", "difficulty": "Medium-High"},
    {"keyword": "dental implant cost bangalore", "intent": "Commercial", "location": "Bangalore", "priority": "High", "contentType": "Supporting Blog #1", "targetPage": "/dental-implant-cost-bangalore", "cpc": "₹114.00", "difficulty": "High"},
    {"keyword": "single tooth implant cost bangalore", "intent": "Transactional", "location": "Bangalore Central", "priority": "High", "contentType": "Supporting Blog #1", "targetPage": "/dental-implant-cost-bangalore", "cpc": "₹86.00", "difficulty": "Medium"},
    {"keyword": "full mouth dental implant cost bangalore", "intent": "Transactional", "location": "Bangalore Metro", "priority": "High", "contentType": "Supporting Blog #1", "targetPage": "/dental-implant-cost-bangalore", "cpc": "₹148.00", "difficulty": "High"},
    {"keyword": "all on 4 dental implant price bangalore", "intent": "Commercial", "location": "Bangalore", "priority": "Medium", "contentType": "Supporting Blog #1", "targetPage": "/dental-implant-cost-bangalore", "cpc": "₹132.00", "difficulty": "Medium"},
    {"keyword": "dental implant procedure timeline bangalore", "intent": "Informational", "location": "Bangalore", "priority": "Medium", "contentType": "Supporting Blog #2", "targetPage": "/dental-implant-timeline-healing", "cpc": "₹42.00", "difficulty": "Low-Med"},
    {"keyword": "how long do dental implants take", "intent": "Informational", "location": "Pan-India / Local", "priority": "High", "contentType": "Supporting Blog #2", "targetPage": "/dental-implant-timeline-healing", "cpc": "₹38.00", "difficulty": "Medium"},
    {"keyword": "stages of dental implant healing", "intent": "Informational", "location": "General", "priority": "Medium", "contentType": "Supporting Blog #2", "targetPage": "/dental-implant-timeline-healing", "cpc": "₹29.00", "difficulty": "Low"},
    {"keyword": "same day dental implants bangalore", "intent": "Commercial", "location": "Bangalore East", "priority": "High", "contentType": "Supporting Blog #2", "targetPage": "/dental-implant-timeline-healing", "cpc": "₹98.00", "difficulty": "Medium"},
    {"keyword": "are dental implants safe", "intent": "Informational", "location": "General", "priority": "High", "contentType": "Supporting Blog #3", "targetPage": "/are-dental-implants-safe", "cpc": "₹34.00", "difficulty": "Medium"},
    {"keyword": "dental implant success rate india", "intent": "Informational", "location": "India / Bangalore", "priority": "Medium", "contentType": "Supporting Blog #3", "targetPage": "/are-dental-implants-safe", "cpc": "₹45.00", "difficulty": "Low"},
    {"keyword": "dental implants for diabetic patients bangalore", "intent": "Informational", "location": "Bangalore", "priority": "High", "contentType": "Supporting Blog #3", "targetPage": "/are-dental-implants-safe", "cpc": "₹62.00", "difficulty": "Medium"},
    {"keyword": "dental implant aftercare instructions", "intent": "Informational", "location": "General", "priority": "Medium", "contentType": "Supporting Blog #4", "targetPage": "/dental-implant-aftercare-guide", "cpc": "₹22.00", "difficulty": "Low"},
    {"keyword": "what to eat after dental implant surgery", "intent": "Informational", "location": "General", "priority": "High", "contentType": "Supporting Blog #4", "targetPage": "/dental-implant-aftercare-guide", "cpc": "₹18.00", "difficulty": "Low"},
    {"keyword": "best implantologist Indiranagar 100ft road", "intent": "Local", "location": "Indiranagar, BLR", "priority": "High", "contentType": "Local Landing / Pillar", "targetPage": "/dental-implants-bangalore", "cpc": "₹120.00", "difficulty": "Medium"},
    {"keyword": "dental implants Whitefield Bangalore", "intent": "Local", "location": "Whitefield, BLR", "priority": "High", "contentType": "Local Landing", "targetPage": "/dental-implants-bangalore", "cpc": "₹94.00", "difficulty": "Medium"},
    {"keyword": "tooth implant cost Koramangala Bangalore", "intent": "Local", "location": "Koramangala, BLR", "priority": "High", "contentType": "Supporting Blog #1", "targetPage": "/dental-implant-cost-bangalore", "cpc": "₹108.00", "difficulty": "Medium"}
]

# Internal Linking dataset
links_data = [
    {"from": "Pillar Blog", "fromUrl": "/dental-implants-bangalore", "to": "Supporting #1 (Cost)", "toUrl": "/dental-implant-cost-bangalore", "anchor": "dental implant cost in Bangalore", "purpose": "Commercial Handoff", "location": "Section 2 & Section 5"},
    {"from": "Pillar Blog", "fromUrl": "/dental-implants-bangalore", "to": "Supporting #2 (Timeline)", "toUrl": "/dental-implant-timeline-healing", "anchor": "dental implant procedure timeline", "purpose": "Procedure Clarity", "location": "Section 4"},
    {"from": "Pillar Blog", "fromUrl": "/dental-implants-bangalore", "to": "Supporting #3 (Safety)", "toUrl": "/are-dental-implants-safe", "anchor": "safety and success rate of dental implants", "purpose": "Risk Mitigation", "location": "Section 3"},
    {"from": "Pillar Blog", "fromUrl": "/dental-implants-bangalore", "to": "Supporting #4 (Aftercare)", "toUrl": "/dental-implant-aftercare-guide", "anchor": "dental implant recovery and aftercare guide", "purpose": "Post-Care Trust", "location": "Section 6"},
    {"from": "Supporting #1 (Cost)", "fromUrl": "/dental-implant-cost-bangalore", "to": "Pillar Blog", "toUrl": "/dental-implants-bangalore", "anchor": "guide to dental implants in Bangalore", "purpose": "PageRank Uplift", "location": "Introduction paragraph"},
    {"from": "Supporting #1 (Cost)", "fromUrl": "/dental-implant-cost-bangalore", "to": "Supporting #3 (Safety)", "toUrl": "/are-dental-implants-safe", "anchor": "safety and success rate of dental implants", "purpose": "Lateral Cross-Link", "location": "Bone Grafting section"},
    {"from": "Supporting #1 (Cost)", "fromUrl": "/dental-implant-cost-bangalore", "to": "Supporting #2 (Timeline)", "toUrl": "/dental-implant-timeline-healing", "anchor": "dental implant procedure timeline guide", "purpose": "Lateral Cross-Link", "location": "Staged Payments section"},
    {"from": "Supporting #2 (Timeline)", "fromUrl": "/dental-implant-timeline-healing", "to": "Pillar Blog", "toUrl": "/dental-implants-bangalore", "anchor": "dental implants in Bangalore", "purpose": "Hub Authority", "location": "Introduction paragraph"},
    {"from": "Supporting #2 (Timeline)", "fromUrl": "/dental-implant-timeline-healing", "to": "Supporting #4 (Aftercare)", "toUrl": "/dental-implant-aftercare-guide", "anchor": "dental implant recovery and aftercare guide", "purpose": "Lateral Cross-Link", "location": "Osseointegration section"},
    {"from": "Supporting #2 (Timeline)", "fromUrl": "/dental-implant-timeline-healing", "to": "Supporting #1 (Cost)", "toUrl": "/dental-implant-cost-bangalore", "anchor": "dental implant cost in Bangalore", "purpose": "Commercial Handoff", "location": "Same-Day Teeth section"},
    {"from": "Supporting #3 (Safety)", "fromUrl": "/are-dental-implants-safe", "to": "Pillar Blog", "toUrl": "/dental-implants-bangalore", "anchor": "dental implants in Bangalore", "purpose": "Hub Authority", "location": "Introduction paragraph"},
    {"from": "Supporting #3 (Safety)", "fromUrl": "/are-dental-implants-safe", "to": "Supporting #4 (Aftercare)", "toUrl": "/dental-implant-aftercare-guide", "anchor": "dental implant recovery and aftercare guide", "purpose": "Lateral Cross-Link", "location": "Failure Prevention section"},
    {"from": "Supporting #4 (Aftercare)", "fromUrl": "/dental-implant-aftercare-guide", "to": "Supporting #2 (Timeline)", "toUrl": "/dental-implant-timeline-healing", "anchor": "dental implant procedure timeline", "purpose": "Educational Continuity", "location": "Warning Signs section"},
    {"from": "Supporting #4 (Aftercare)", "fromUrl": "/dental-implant-aftercare-guide", "to": "Pillar Blog", "toUrl": "/dental-implants-bangalore", "anchor": "dental implants in Bangalore", "purpose": "Hub Uplift", "location": "Conclusion section"}
]

# Recent Projects
projects_data = [
    {
        "id": "proj-1",
        "name": "Dental Implants Bangalore",
        "business": "BrightSmile Dental Clinic",
        "type": "Healthcare / Dental",
        "primaryKeyword": "dental implants in bangalore",
        "clusterSize": "1 Pillar + 4 Supporting",
        "status": "Published",
        "updated": "Today at 5:15 PM",
        "localArea": "Indiranagar, Bangalore"
    },
    {
        "id": "proj-2",
        "name": "JEE Advanced Foundation Kota",
        "business": "Apex JEE & NEET Academy",
        "type": "Education & Test Prep",
        "primaryKeyword": "best jee coaching in kota",
        "clusterSize": "1 Pillar + 3 Supporting",
        "status": "In Progress",
        "updated": "Yesterday",
        "localArea": "Kota & Jaipur, RJ"
    },
    {
        "id": "proj-3",
        "name": "Customer Support AI Automation",
        "business": "NexaFlow SaaS",
        "type": "B2B SaaS / CX",
        "primaryKeyword": "customer support automation software",
        "clusterSize": "1 Pillar + 5 Supporting",
        "status": "Review",
        "updated": "3 days ago",
        "localArea": "Global English / BLR"
    }
]

print("Injecting data into template.html...")

final_html = template_html.replace("__ARTICLES_DATA__", json.dumps(articles_data).replace("</script>", "<\\/script>"))
final_html = final_html.replace("__KEYWORDS_DATA__", json.dumps(keywords_data).replace("</script>", "<\\/script>"))
final_html = final_html.replace("__LINKS_DATA__", json.dumps(links_data).replace("</script>", "<\\/script>"))
final_html = final_html.replace("__PROJECTS_DATA__", json.dumps(projects_data).replace("</script>", "<\\/script>"))
final_html = final_html.replace("__LOCAL_SCHEMA__", json.dumps(schema_part).replace("</script>", "<\\/script>"))

index_path = os.path.join(base_dir, "index.html")
preview_path = os.path.join(base_dir, "preview", "index.html")

print(f"Writing index.html ({len(final_html)} bytes)...")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Copying to preview/index.html...")
shutil.copyfile(index_path, preview_path)

print("Build completed successfully via template injection!")
