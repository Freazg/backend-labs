@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)
    
    if user_id is None and category_id is None:
        return jsonify({'error': 'user_id or category_id parameter is required'}), 400
    
    filtered_records = []
    for record in records.values():
        match = False
        
        if user_id is not None and category_id is not None:
            if record['user_id'] == user_id and record['category_id'] == category_id:
                match = True
        elif user_id is not None:
            if record['user_id'] == user_id:
                match = True
        elif category_id is not None:
            if record['category_id'] == category_id:
                match = True
        
        if match:
            filtered_records.append(record)
    
    return jsonify(filtered_records), 200
