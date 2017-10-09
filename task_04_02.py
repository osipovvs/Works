def http_headers_to_json(inp, out):
    import json

    with open(inp) as headers:
        heads = headers.readlines()
    
    newheads = []
    respond = heads[0].startswith("HTTP/")

    for i in range(len(heads)):
        border = heads[i].find(': ')
        if border != -1:
            left_part = (heads[i])[:border]
            right_part = (heads[i])[(border + 2):]
            line_list = [left_part, right_part]
            newheads.append(line_list)

    common_headers = {newheads[i][0]: (newheads[i][1].replace('\n', '')) for i in range(len(newheads))}

    if respond:
        first_str = heads[0].split(' ')
        st_message = list(first_str)[2:len(list(first_str))]  # handling multi-word statuses. 
        # List 'heads' is a list of strings (the headers from the input file). Status message is in the first string (heads[0]). It is
        # preceded by two elements (i.e. words): heads[0][0] and heads[0][1] and lasts till the end of the line. Thus, we start
        # from heads[0][2] and finish with the length of heads[0] splitted by spaces (i.e. a list assembled from the words of the 
        # input's file first string).
        
        responce_headers = {
            "protocol": first_str[0],
            "status_message": (' '.join(st_message)).replace('\n', ''),
            "status_code": first_str[1]
        }
        output = dict(common_headers, **responce_headers)
    else:
        first_str = heads[0].split(' ')

        request_headers = {
            "method": first_str[0],
            "uri": first_str[1],
            "protocol": first_str[2].replace('\n', '')
        }

        output = dict(common_headers, **request_headers)

    with open (out, 'w') as outs:
        json.dump(output, outs, indent = 4) # indent > 0 is set to print the output line by line, not inline
