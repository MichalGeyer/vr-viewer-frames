# import os

# VIEWERS_DIR = "./viewers"
# OUTPUT_INDEX = "index.html"  # Where we'll write the generated HTML

# # HTML skeleton
# HTML_HEAD = """<!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <title>3D Viewer</title>
#   <style>
#     /* Basic reset or box-sizing if desired */
#     * {
#       margin: 0;
#       padding: 0;
#       box-sizing: border-box;
#     }

#     /* Center everything on the page */
#     body {
#       display: flex;
#       flex-direction: column;
#       align-items: center;
#       font-family: sans-serif;
#       min-height: 100vh;
#       background-color: #f5f5f5;
#       padding: 20px;
#     }

#     /* Heading styling */
#     h1 {
#       margin: 20px 0;
#     }

#     /* Thumbnails container */
#     .thumbnails {
#       display: flex;
#       flex-wrap: wrap;  /* allow wrapping if many folders */
#       gap: 20px;        /* space between each thumbnail */
#       max-width: 1200px;
#       justify-content: center;
#     }

#     /* Individual thumbnail link */
#     .thumbnail {
#       text-align: center;
#       text-decoration: none;
#       color: #333;
#       background-color: #fff;
#       border: 1px solid #ddd;
#       padding: 10px;
#       border-radius: 8px;
#       transition: box-shadow 0.3s ease;
#       width: 180px;
#     }

#     .thumbnail:hover {
#       box-shadow: 0 0 10px rgba(0,0,0,0.2);
#     }

#     /* Image styling */
#     .thumbnail img {
#       width: 150px;
#       height: auto;
#       display: block;
#       margin: 0 auto 10px;
#     }

#     /* Caption styling */
#     .thumbnail p {
#       margin-top: 5px;
#       font-size: 14px;
#     }
#   </style>
# </head>
# <body>
#   <h1>3D Viewer</h1>
#   <div class="thumbnails">
# """

# HTML_FOOT = """  </div>
# </body>
# </html>
# """

# def parse_folder_name(folder_name: str):
#     """
#     Extracts the prompt and the type (ours or depthcrafter)
#     based on folder name patterns:
#       - something_ours
#       - something_depthc
#     Returns:
#       (prompt, label)
#       e.g., ("A_modern_glass_building", "ours") 
#             ("Another_prompt", "depthcrafter")
#     """
#     if folder_name.endswith("_ours"):
#         prompt = folder_name[:-5]  # remove "_ours"
#         label = "ours"
#     elif folder_name.endswith("_depthc"):
#         prompt = folder_name[:-7]  # remove "_depthc"
#         label = "depthcrafter"
#     elif folder_name.endswith("_warp_inpaint"):
#         prompt = folder_name[:-(len("_warp_inpaint"))]  # remove "_depthc"
#         label = "warp_inpaint"
#     elif folder_name.endswith("_comparison_spatial"):
#         prompt = folder_name[:-(len("_comparison_spatial"))]
#         label = "comparison_spatial"
#     elif folder_name.endswith("_comparison_temporal"):
#         prompt = folder_name[:-(len("_comparison_temporal"))]
#         label = "comparison_temporal"
#     else:
#         prompt = folder_name
#         label = "unknown"
#     return prompt, label

# def generate_thumbnail_html(folder_name: str, prompt: str, label: str) -> str:
#     """
#     Returns the HTML snippet for a single thumbnail entry.
#     Assumes thumbnail is at ./viewers/<folder_name>/thumbnail.png
#     and index.html is at ./viewers/<folder_name>/index.html
#     """
#     relative_folder_path = os.path.join("viewers", folder_name)
#     thumbnail_path = os.path.join(relative_folder_path, "thumbnail.png")
#     index_path = os.path.join(relative_folder_path, "index.html")

#     # alt text is "<prompt> ours" or "<prompt> depthcrafter"
#     alt_text = f"{prompt} {label}"
#     # <img src="{thumbnail_path}" alt="{alt_text}" />
#     html_snippet = f"""    <a class="thumbnail" href="{index_path}">
#       <img src='https://michalgeyer.github.io/vr-viewer-files-webm/pairs-user-study-webm/images/{prompt}.png' alt="{alt_text}" />
#       <p>{label}</p>
#     </a>
# """
#     return html_snippet

# def main():
#     # Gather all subfolders in ./viewers
#     viewer_folders = []
#     for item in os.listdir(VIEWERS_DIR):
#         if item.endswith('depthc') or '.DS' in item or item == 'images':
#             continue
#         # if not item.endswith('_comparison_spatial'):
#         #     continue
#         full_path = os.path.join(VIEWERS_DIR, item)
#         if os.path.isdir(full_path):
#             viewer_folders.append(item)

#     # Build up the thumbnail HTML
#     thumbnails_html = ""
#     for folder in sorted(viewer_folders):
#         prompt, label = parse_folder_name(folder)
#         # If you only want to include known types, skip unknown:
#         # if label == "unknown":
#         #     continue

#         thumbnails_html += generate_thumbnail_html(folder, prompt, label)

#     # Wrap with HEAD and FOOT
#     final_html = HTML_HEAD + thumbnails_html + "\n" + HTML_FOOT

#     # Write out the index.html file
#     with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
#         f.write(final_html)

#     print(f"Generated {OUTPUT_INDEX} with {len(viewer_folders)} entries.")

# if __name__ == "__main__":
#     main()


import os

VIEWERS_DIR = "./viewers"
OUTPUT_INDEX = "index.html"  # Where we'll write the generated HTML

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>3D Viewer Navigator</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #f5f5f5;
      font-family: sans-serif;
    }

    h1 {
      margin-bottom: 20px;
    }

    .button {
      background-color: #2E7D32;
      color: #fff;
      border: none;
      padding: 10px 20px;
      margin: 5px;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.2s;
    }
    .button:hover {
      background-color: #1b5e20;
    }

    .viewer-container {
      display: none;
      flex-direction: column;
      align-items: center;
    }

    iframe {
      width: 80vw;
      height: 60vh;
      border: 2px solid #ddd;
      border-radius: 8px;
      background-color: #fff;
      margin-bottom: 20px;
    }

    .nav-buttons {
      display: flex;
      gap: 20px;
    }
  </style>
</head>
<body>
  <h1>3D Viewer Navigator</h1>
  <button id="startButton" class="button">Start</button>
  <div class="viewer-container" id="viewerContainer">
    <iframe id="viewerFrame" src="" frameborder="0"></iframe>
    <div class="nav-buttons">
      <button id="prevButton" class="button">&larr; Prev</button>
      <button id="nextButton" class="button">Next &rarr;</button>
    </div>
  </div>

  <script>
    // Array of viewer URLs
    const viewerUrls = [
"""

HTML_FOOT = """    ];

    let currentIndex = 0;

    const startButton = document.getElementById('startButton');
    const viewerContainer = document.getElementById('viewerContainer');
    const viewerFrame = document.getElementById('viewerFrame');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');

    function showViewer(index) {
      viewerFrame.src = viewerUrls[index];
    }

    startButton.addEventListener('click', () => {
      startButton.style.display = 'none';
      viewerContainer.style.display = 'flex';
      currentIndex = 0;
      showViewer(currentIndex);
    });

    nextButton.addEventListener('click', () => {
      if (currentIndex < viewerUrls.length - 1) {
        currentIndex++;
        showViewer(currentIndex);
      }
    });

    prevButton.addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
        showViewer(currentIndex);
      }
    });
  </script>
</body>
</html>
"""

def parse_folder_name(folder_name: str):
    """Extracts the prompt and the type based on folder name patterns."""
    if folder_name.endswith("_comparison_spatial"):
        prompt = folder_name[:-(len("_comparison_spatial"))]
        label = "comparison_spatial"
    elif folder_name.endswith("_comparison_temporal"):
        prompt = folder_name[:-(len("_comparison_temporal"))]
        label = "comparison_temporal"
    else:
        prompt = folder_name
        label = "unknown"
    return prompt, label

def main():
    # Gather all subfolders in ./viewers
    viewer_folders = []
    for item in os.listdir(VIEWERS_DIR):
        if item.endswith('depthc') or '.DS' in item or item == 'images':
            continue
        full_path = os.path.join(VIEWERS_DIR, item)
        if os.path.isdir(full_path):
            viewer_folders.append(item)

    # Generate viewer URLs
    viewer_urls = ""
    for folder in sorted(viewer_folders):
        prompt, label = parse_folder_name(folder)
        index_path = os.path.join("viewers", folder, "index.html").replace("\\", "/")
        viewer_urls += f'      "{index_path}",\n'

    # Combine HTML parts
    final_html = HTML_HEAD + viewer_urls.rstrip(",\n") + "\n" + HTML_FOOT

    # Write out the HTML file
    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Generated {OUTPUT_INDEX} with {len(viewer_folders)} entries.")

if __name__ == "__main__":
    main()