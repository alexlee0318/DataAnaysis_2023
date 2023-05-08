import os
import numpy as np
from PIL import Image

# Pillow format의 img를 읽어서 중심부의 정사각형 이미지를 pillow format으로 반환 
def center_image(img):
    h, w, _ = np.array(img).shape
    diff = abs(h - w) // 2
    if w > h:           # landscape image
        final_img = np.array(img)[:, diff:diff+h, :]    # 슬라이싱
    else:               # portrait image
        final_img = np.array(img)[diff:diff+w, :, :]
    return Image.fromarray(final_img)

def change_profile(app, filename):
    img = Image.open(filename)
    new_fname = os.path.join(app.static_folder, 'data/profile.png')
    center_image(img).save(new_fname, format='png')
    return os.stat(new_fname).st_mtime  # mtime : 파일이 최종 수정된시각