from flask import Flask, jsonify, request, make_response
from filesystem_ops import FileSystemOps

fs_ops = FileSystemOps(directory_path="data")

app=Flask(__name__)

@app.route("/create/<string:file_name>",methods=["POST"])
def create(file_name):
    try:
        if fs_ops.create_file(file_name=file_name, data=request.data):
            return jsonify({"result": "success"}), 201
        else:
            return jsonify({"result": "failed"}), 304
    except Exception as e:
        print(f"create :: error occured :: {e}")
        return jsonify({"result": "failed"}), 500

@app.route("/delete/<string:file_name>",methods=["DELETE"])
def delete(file_name):
    try:
        if fs_ops.delete_file(file_name=file_name):
            return jsonify({"result": "success"}), 201
        else:
            return jsonify({"result": "failed"}), 304

    except Exception as e:
        print(f"delete :: error occured :: {e}")
        return jsonify({"result": "failed"}), 500

@app.route("/update/<string:file_name>",methods=["PUT"])
def update(file_name):
    try:
        result = fs_ops.update_file(file_name=file_name, data = request.data)
        if result:
            return jsonify({"result":"success"}), 201
        elif result == None:
            return jsonify({"result":"file not found"}), 404
        else:
            return jsonify({"result":"failed"}), 304
    except Exception as e:
        print(f"update :: error occured :: {e}")
        return jsonify({"result":"failed"}), 500

@app.route("/file/<string:file_name>",methods=["GET"])
def get(file_name):
    try:
        data = fs_ops.read_file(file_name=file_name)
        if data != None:
            response = make_response(data)
            response.headers["Content-Type"] = "application/octet-stream"
            # mime_type = magic.from_buffer(data, mime=True)
            # response.headers["Content-Type"] = mime_type
            return response, 200
        else:
            return jsonify({"result": "file not found"}), 404
    except Exception as e:
        print(f"list :: error occured :: {e}")
        return jsonify({"result": "server error"}), 500

@app.route("/list",methods=["GET"])
def list():
    try:
        return jsonify({"result": fs_ops.list_files()}), 200
    except Exception as e:
        print(f"list :: error occured :: {e}")
        return jsonify({"result": []}), 500


if __name__=="__main__":
    app.run(host="0.0.0.0",port=9000,debug=True)