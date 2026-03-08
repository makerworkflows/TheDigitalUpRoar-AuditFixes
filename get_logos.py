import os
import requests
from io import BytesIO
from PIL import Image
from rembg import remove

# Define the absolute original URLs from the virtual tours page
logo_urls = [
    "https://static.wixstatic.com/media/cf0155_16877fabc67f4e75b2564c76166e4cd1~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/LOGO.jpg",
    "https://static.wixstatic.com/media/cf0155_614d9f606e3a4ba889f940a5ba3ad2ed~mv2.jpg/v1/fill/w_420,h_420,al_c,lg_1,q_80,enc_avif,quality_auto/50%20eggs%20logo.jpg",
    "https://static.wixstatic.com/media/cf0155_ec64a9a16e2b4197bbbddd092096eec3~mv2.jpg/v1/fill/w_720,h_720,al_c,lg_1,q_85,enc_avif,quality_auto/VT%20LOGO.jpg",
    "https://static.wixstatic.com/media/cf0155_df4e07f662214c339ba7103e40787b99~mv2.png/v1/fill/w_339,h_235,al_c,lg_1,q_85,enc_avif,quality_auto/Pershing_RGB_Primary-Logo_Trumpet-Gold.png",
    "https://static.wixstatic.com/media/cf0155_d698c17219ee45cb8487c4785e7baae5~mv2.jpeg/v1/fill/w_560,h_560,al_c,lg_1,q_80,enc_avif,quality_auto/xalbW5p4_400x400.jpeg",
    "https://static.wixstatic.com/media/cf0155_c9f8ea3d40c243cea69ba58777b9f1b4~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/VT%20logo%20file.jpg",
    "https://static.wixstatic.com/media/cf0155_bfcf14a78a884c1d815648b5b089b8e0~mv2.png/v1/fill/w_274,h_274,al_c,lg_1,q_85,enc_avif,quality_auto/driscoll%20happy%20sun.png",
    "https://static.wixstatic.com/media/cf0155_5facd6d733fe4d62a82d48f37a51ce07~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/UDTL%20VT%20logo%20file.jpg",
    "https://static.wixstatic.com/media/cf0155_6424d2379de84704a2a080363c00cb50~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/2022%20VT%20LOGO%20jpg.jpg",
    "https://static.wixstatic.com/media/cf0155_0d56d403c481408ea8465580b1c41425~mv2.jpg/v1/fill/w_768,h_768,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/VT%20logo%20file.jpg",
    "https://static.wixstatic.com/media/cf0155_f225a37c3b024a36a73be1760b5d6eda~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/VT%20LOGO%20jpg.jpg",
    "https://static.wixstatic.com/media/cf0155_2b559f74bdcd45d182cd129e28c3e921~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/carmel%20sports%20club%20fb%20logo.jpg",
    "https://static.wixstatic.com/media/cf0155_0eb2a346d9ca4891a1d3fe9296246e22~mv2.png/v1/fill/w_782,h_782,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/CITY%20OF%20PHARR%20-%20LOGO%20no%20bg.png",
    "https://static.wixstatic.com/media/cf0155_b462d1d0611f41329789bf536e05f541~mv2.jpg/v1/fill/w_800,h_800,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/old%20logo%20VT%20file.jpg"
]

filenames = [
    "tao.png", "50eggs.png", "neuehouse.png", "pershing.png", "goldgirl.png", "maxpawn.png", "driscoll.png", "udtl.png", "mcallen.png", "haitian.png", "commonground.png", "carmel.png", "pharr.png", "amelyoussef.png"
]

# Ensure output directory exists (we put them straight into assets/logos if we want, or root)
os.makedirs("assets/logos", exist_ok=True)

for i, url in enumerate(logo_urls):
    filename = filenames[i]
    filepath = os.path.join("assets/logos", filename)
    print(f"Processing {filename}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Check if already a pure PNG transparent url like pershing or driscoll
        if url.endswith('.png') or 'no bg' in url.lower():
            # Simply save it
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Saved natively transparent logo: {filename}")
        else:
            # Run rembg to remove the background
            input_image = Image.open(BytesIO(response.content))
            output_image = remove(input_image)
            output_image.save(filepath, "PNG")
            print(f"Successfully processed and removed background: {filename}")
            
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

print("Logo background extraction complete.")
