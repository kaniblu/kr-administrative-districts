# encoding: utf-8

import json


if __name__ == "__main__":        
    with open("original/districts.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    json_data = {
        "name": "korean-admin-districts",
        "version": "20170824",
        "url": "https://github.com/kaniblu/korean-admin-districts",
        "data": {
            "districts": {}
        }
    }
    for line in lines:
        tokens = line.split(",")
        
        print(tokens)
        
        if len(tokens) != 10:
            continue
        
        if not tokens[1]:
            continue
            
        major_code = int(tokens[1])
        major_name_ko = tokens[2].strip()
        
        # 시도
        if not tokens[3] or tokens[3] == str(major_code):
            major_name_en = tokens[-3].strip()
            major_name_hj = tokens[-2].strip()
            
            json_data["data"]["districts"][major_name_ko] = {
                "name_ko": major_name_ko,
                "name_en": major_name_en,
                "name_hj": major_name_hj,
                "code": major_code,
                "type": "major",
                "districts": {}
            }
                
            continue
            
        median_code = int(tokens[3])
        median_name_ko = tokens[4].strip()
        
        # 시군구
        if not tokens[5] or tokens[5] == str(median_code):
            median_name_en = tokens[-3].strip()
            median_name_hj = tokens[-2].strip()
            
            json_data["data"]["districts"][major_name_ko]["districts"][median_name_ko] = {
                "name_ko": median_name_ko,
                "name_en": median_name_en,
                "name_hj": median_name_hj,
                "code": median_code,
                "type": "median",
                "districts": {}
            }
               
            continue
            
        minor_code = int(tokens[5])
        minor_name_ko = tokens[6].strip()
        minor_name_en = tokens[-3].strip()
        minor_name_hj = tokens[-2].strip()
        
        json_data["data"]["districts"][major_name_ko]["districts"][median_name_ko]["districts"][minor_name_ko] = {
            "name_ko": minor_name_ko,
            "name_en": minor_name_en,
            "name_hj": minor_name_hj,
            "code": minor_code,
            "type": "minor"
        }
        
    with open("districts.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)