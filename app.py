import os
import tempfile

import cv2
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

from watershed import count_trees


app = Flask(__name__)


ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/test")
def test():
    return "Your Flask app is running."


@app.route("/countPalmTrees", methods=["POST"])
def countPalmTrees():
    if "file" not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    image = request.files["file"]
    if image.filename == "":
        return jsonify({"message": "No file selected for uploading"}), 400
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        with tempfile.TemporaryDirectory() as tmpdirname:
            img_path = os.path.join(tmpdirname, filename)
            image.save(img_path)
            tagged_img, label_cnt = count_trees(img_path)
            if "image" in request.form.to_dict():
                if request.form.to_dict()["image"].lower() == "yes":
                    op_path = os.path.join(tmpdirname, "output.png")
                    cv2.imwrite(op_path, tagged_img)
                    return send_file(op_path)
            return jsonify({"tree_count": label_cnt}), 200
    else:
        return (
            jsonify({"message": "Allowed file types are png, jpg, jpeg"}),
            400,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8360, debug=True)
