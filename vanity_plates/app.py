from database import app,SessionLocal
from flask import request, jsonify
from model import VanityPlate,select

@app.route("/plate/insert",methods=["POST"])
def insert_license_plate():
    data = request.get_json()
    #check license plate length
    plate_number = str(data["plate_number"])
    if len(plate_number) < 2 or len(plate_number) > 6:
        return jsonify({
            "code":500,
            "msg":"Invalid"
        })
    #check whether both the first and second charcaters are letters
    if not plate_number[0:2].isalpha():
        return jsonify({
            "code":500,
            "msg":"Invalid"
        })
    #check plate whether only has letters and numbers
    if not plate_number.isalnum():
         return jsonify({
            "code":500,
            "msg":"Invalid"
        })
    # check the first digit whether is 0
    for c in plate_number[2:]:
        if c.isdigit():
            if c == "0":
                print(c)
                return jsonify({
            "code":500,
            "msg":"Invalid"
            })
            else:
                break
        else:
            break

    owner = str(data["owner"])
    db = SessionLocal() 
    #check current owner whether has license plate
    owner_plate = db.scalar(select(VanityPlate).where(VanityPlate.owner == owner))
    if owner_plate is not None:
        return jsonify({
            "code":500,
            "msg":"every person only has one plate number"
            })
    #check this plate number whether has been registered
    plates = db.scalars(select(VanityPlate).where(VanityPlate.owner != owner,
                                                          VanityPlate.license_plate_number == plate_number)).all()
    if len(plates) != 0:
        return jsonify({
        "code":500,
        "msg":"This plate number has been registered."
        })
    # add data into database

    try:
        new_plate = VanityPlate(
            license_plate_number = plate_number,
            owner = owner
        )
        db.add(new_plate)
        db.commit()
        return jsonify(
            {
                "code":200,
                "msg":"Valid"
            }
        )
    except Exception as e:
        db.rollback()
        print(e)
        return jsonify(
            {"code":500,
             "msg":"server error"}
        )        

@app.route('/plate/list', methods=['GET'])
def plate_list():
    db = SessionLocal() 
    plate_list = db.scalars(select(VanityPlate)).all()
    result = []
    for item in plate_list:
        result.append(
            {
                "id":item.id,
                "plate_number":item.license_plate_number,
                "owner":item.owner
            }
        )
    return jsonify(
        {"code":200,
         "data":result}
    )    

if __name__ == "__main__":
    app.run(debug=True)