from openai import OpenAI
import datetime
import json

client = OpenAI(api_key="")

with open('data.json', encoding="utf-8") as f:
  dataFlight = json.load(f)

def gptService(userContent):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a customer support assistant at the Tân Sơn Nhất airport."},
            {"role": "system", "content": "You can also become a tour guide."},
            {"role": "system", "content": "You answer briefly in one sentence."},
            {"role": "user", "content": userContent}
        ],
            max_tokens=271, 
            n=1,
            temperature=1
    )

    return response.choices[0].message.content

def time():
    timeCurrent = [datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year]
    
    return timeCurrent  

def checkDayTimeData():
    dataTemp = []#ngày, tháng, giờ, phút
    dayTemp = False
    for i in dataFlight[0]["chuyen_bay"]["khoi_hanh"]["ngay"].split():
        if dayTemp:
            dataTemp.append(i)
        dayTemp = False
        if i == "ngày":
            dayTemp =True
        if i == "tháng":
            dayTemp =True
    
    timeTemp = ""
    timeTemp += dataTemp[0]["chuyen_bay"]["khoi_hanh"]["thoi_gian"][0]
    timeTemp += dataTemp[0]["chuyen_bay"]["khoi_hanh"]["thoi_gian"][1]
    dataTemp.append(timeTemp)
    timeTemp = ""
    timeTemp += dataTemp[0]["chuyen_bay"]["khoi_hanh"]["thoi_gian"][3]
    timeTemp += dataTemp[0]["chuyen_bay"]["khoi_hanh"]["thoi_gian"][4]
    dataTemp.append(timeTemp)

    return dataTemp

# def checkFlightNow() -> bool:
#     pass


#     if  (time()[3] == int(dataTemp[0])) and (time()[4] == int(dataTemp[1])):
#         if  (time()[0] == int(dataTemp[2])) and (time()[1] <= int(dataTemp[3])):
#             return True
#         elif  (time()[0] == int(dataTemp[2])):
#             return True
    
#     return False

# def checkFlightFromTimeToTime(userContent) -> bool:
#     dataTemp = []#ngày, tháng
#     dayTemp = False
#     for i in dataFlight[0]["chuyen_bay"]["khoi_hanh"]["ngay"].split():
#         if dayTemp:
#             dataTemp.append(i)
#         dayTemp = False
#         if i == "ngày":
#             dayTemp =True
#         if i == "tháng":
#             dayTemp =True

#     splitContent = userContent.split()
#     temp = ""
#     tempType = "giờ"

#     for i in splitContent:
#         if temp != "":
#             temp = i
#             break
#         if ("ngày" in userContent):
#             if (i == "ngày"):
#                 temp = i
#         else:
#             if (i == "lúc") or (i == "vào") or (i == "khoảng") or (i == "tại"):
#                 temp = i

#     if ("giờ" in userContent):
#         tempType = "giờ"

#     if ("ngày" in userContent):
#         tempType = "ngày"

#     if tempType == "giờ":
#         if (time()[3] <= int(dataTemp[0])) and (time()[4] == int(dataTemp[1])) and  ==  temp:
#         if str(time()[3]) <= ngày && str(time()[4]) == tháng && (time()[5]) == năm && str(time()[0]) ==  temp
#                 answer = "Sau đây là danh sách chuyến bay theo thời gian hiện có."
#     elif tempType == "ngày"
#             if temp == "mai"
#                 temp = time()[3] + 1
#             if temp == "mốt"
#                 temp = time()[3] + 2
#         str(time()[3]) == temp && str(time()[4]) <= tháng && (time()[5]) == năm
#             answer = "Sau đây là danh sách chuyến bay theo thời gian hiện có."


def assistantModel_Vi(userContent):
    #Greeting
    if userContent == "":
        answer = "Xin lỗi, tôi không nghe rõ."
    elif (("hello" in userContent) or ("hi" in userContent) or ("xin chào" in userContent)):   
        answer = "Xin chào, tôi là trợ lý ảo hỗ trợ tại cảng hàng không."
    elif (("bye" in userContent) or ("goodbye" in userContent) or ("tạm biệt" in userContent)):   
        answer = "Tạm biệt quý khách hàng."
    elif ((("mấy" in userContent) or ("nhiêu" in userContent)) 
          and (("giờ" in userContent) or ("thời gian" in userContent) or ("phút" in userContent) or ("giây" in userContent)) 
          and ("hiện" in userContent)):
        answer = "Hiện tại là " + str(time()[0]) + " giờ " + str(time()[1]) + " phút theo giờ Việt Nam."
    ############
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))
          and (("âm" in userContent) or ("ta" in userContent))):
        answer = "Xin lỗi tôi không có kiến thức sử dụng lịch âm, xin lỗi vì sự bất tiện."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))):
        answer = "Hôm nay là ngày " + str(time()[3]) + " tháng " + str(time()[4]) + " năm " + str(time()[5]) + "."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("thứ" in userContent) or (("ngày" in userContent) and ("tuần" in userContent)))
          and (("hiện" in userContent) or ("nay" in userContent))):
        answer = gptService("ngày " + str(time()[3]) + " tháng " + str(time()[4]) + " năm " + str(time()[5]) + "là thứ mấy")
    ###############
    elif (("bạn" in userContent) 
          and (("tên" in userContent) or ("là" in userContent) or ("gì" in userContent))):
        answer = "Tôi là trợ lý ảo được tạo ra bởi khoa Công nghệ thông tin Học viện Hàng không Việt Nam, tôi chưa được đặt tên."
    #############
    elif (("thông tin" in userContent) 
          and ((("của" in userContent) or ("là" in userContent) or ("tên" in userContent))
                and ("tôi" in userContent))):
        answer = "Vui lòng đến quầy dịch vụ gần nhất để có thể biết chi tiết thông tin."
    ##############

    #Maps
    elif ((("khu" in userContent) or ("vị trí" in userContent) or ("chổ" in userContent) or ("đâu" in userContent) or ("đến" in userContent)) 
          and ("quầy" in userContent)):
        answer = "Đây là khu vực quầy thủ tục tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show quầy thủ tục.
    elif ("nhà vệ sinh" in userContent):
        answer = "Đây là một số nhà vệ sinh tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show nhà vệ sinh.
    elif ((("cổng" in userContent) or ("cửa" in userContent) or ("lối" in userContent)) 
          and (("bay" in userContent) or ("khởi hành" in userContent) or ("số" in userContent))):
        answer = "Đây là một số cửa tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show toàn bộ cửa.
    elif ((("cổng" in userContent) or ("cửa" in userContent) or ("lối" in userContent)) 
          and (("thoát" in userContent) or ("rời" in userContent)  or ("ra" in userContent))):
        answer = "Đây là một số lối rời cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show toàn bộ cửa ra ngoài.
    elif ((("khu" in userContent) or ("vị trí" in userContent) or ("chổ" in userContent) or ("đâu" in userContent) or ("đến" in userContent)) 
          and (("hải quan" in userContent) or ("thủ tục xuất cảnh" in userContent))):
        answer = "Đây là khu vực hải quan tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show khu vực hải quan.
    elif ((("khu" in userContent) or ("vị trí" in userContent) or ("chổ" in userContent) or ("đâu" in userContent) or ("đến" in userContent)) 
          and (("y tế" in userContent) or ("thương" in userContent) or ("bệnh" in userContent))):
        answer = "Đây là khu vực y tế tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show khu vực y tế.
    elif ("thang" in userContent):
        answer = "Đây là một số vị trí thang bộ và thang máy tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show thang.
    elif ((("khu" in userContent) or ("vị trí" in userContent) or ("chổ" in userContent) or ("đâu" in userContent)) 
          and (("nhà hàng" in userContent) or ("ăn" in userContent) or ("nước" in userContent) or ("uống" in userContent)  or ("cửa hàng" in userContent))):
        answer = "Đây là khu vực nhà hàng và cửa hàng tiện lợi tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show nhà hàng.
    elif (("khu" in userContent) or ("vị trí" in userContent) or ("chổ" in userContent) or ("đâu" in userContent or ("đến" in userContent))
          and ("hãng" in userContent)):
        answer = "Đây là khu vực một số hãng hàng không tại cảng hàng không, chúng sẽ được thể hiện trên bản đồ."
        #Gọi hàm bật map và show hãng hàng không.

    #Flight
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) and ("của tôi" in userContent)):
        answer = "Vui lòng đến quầy dịch vụ gần nhất để có thể biết chi tiết thông tin."
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) and (("hôm nay" in userContent) or ("hiện tại" in userContent) or ("bây giờ" in userContent))):
        if checkFlightNow():
            answer = "Sau đây là danh sách chuyến bay ngày hôm nay."
        else:
            answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
        #Gọi hàm bật lịch bay
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) 
          and (("vào" in userContent) or ("lúc" in userContent) or ("khoảng" in userContent) or ("giờ" in userContent) or ("ngày" in userContent))):
        answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
        # splitContent = userContent.split()
        # temp = ""
        # tempType = "giờ"
        # for i in splitContent:
        #     if i == "giờ":
        #         tempType = "giờ"
        #         break
        #     if i == "ngày":
        #         temp = i
        #         tempType = "ngày"
        #         break
        # if tempType == "giờ":
        #     if str(time()[3]) <= ngày && str(time()[4]) == tháng && (time()[5]) == năm && str(time()[0]) ==  temp
        #          answer = "Sau đây là danh sách chuyến bay theo thời gian hiện có."
        # elif tempType == "ngày"
        #       if temp == "mai"
        #          temp = time()[3] + 1
        #       if temp == "mốt"
        #          temp = time()[3] + 2
        #     str(time()[3]) == temp && str(time()[4]) <= tháng && (time()[5]) == năm
        #         answer = "Sau đây là danh sách chuyến bay theo thời gian hiện có."
        #Gọi hàm bật lịch bay
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) and (("điểm đáp" in userContent) or ("đến" in userContent))):
        answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
        # city = ["bình định", "bình dương"]
        # country = ["việt nam", "trung quốc"]
        # for i in city:
        #     if i in userContent:
        #         city = i
        
        # for i in country:
        #     if i in userContent:
        #         country = i
        
        # if city in danh sách tp:
        #     answer = "Sau đây là danh sách chuyến bay theo địa điểm hiện có."
        #     
        # elif country in danh sách quốc gia:
        #     answer = "Sau đây là danh sách chuyến bay theo địa điểm hiện có."
        #     
        #Gọi hàm bật lịch bay
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) and (("hãng" in userContent) or ("của" in userContent))):
        answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
        # airlines = ["vietjet", "..."]
        # for i in airlines:
        #     if i in userContent:
        #         airlines = i

        
        # if airlines in danh sách tp:
        #     answer = "Sau đây là danh sách chuyến bay theo hãng hàng không hiện có."
        #        
        #Gọi hàm bật lịch bay

    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) 
          and (("dưới" in userContent) or ("trên" in userContent) or (("giá" in userContent) and ("khoảng" in userContent)))):
        answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
        # splitContent = userContent.split()
        # temp = ""
        # tempType = "trên"
        # for i in splitContent:
        #     if (i == "trên") or (i == "khoảng"):
        #         temp = i
        #         tempType = "trên"
        #         break
        #     if i == "dưới":
        #         temp = i
        #         tempType = "dưới"
        #         break

        # if tempType == "trên":
        #          answer = "Sau đây là danh sách chuyến bay theo chi phí hiện có."
        # elif tempType == "dưới"
        #     str(time()[3]) == temp && str(time()[4]) <= tháng && (time()[5]) == năm
        #         answer = "Sau đây là danh sách chuyến bay theo chi phí hiện có."
        #Gọi hàm bật lịch bay

    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent)) 
          and ("bay" in userContent)):
        answer = "Sau đây là danh sách chuyến bay hiện có."
        #Gọi hàm bật lịch bay

        

    #GPT Service
    else:
        answer = gptService(userContent)

    return answer

def assistantModel_En(userContent):
    #Greeting
    if userContent == "":
        answer = "Sorry I didn't quite hear that."
    elif (("hello" in userContent) or ("hi" in userContent) or ("xin chào" in userContent)):   
        answer = "Hi, I'm a support virtual assistant at the airport."
    elif (("bye" in userContent) or ("goodbye" in userContent) or ("tạm biệt" in userContent)):   
        answer = "Goodbye to our valued customers."
    elif ((("time" in userContent)) 
          and ("what" in userContent) or (("now" in userContent) and ("current" in userContent))):
        answer = "It is " + str(time()[0]) + ":" + str(time()[1]) + " Vietnam time."
    elif ((("you" in userContent) or ("your" in userContent))
          and (("name" in userContent) or ("call you" in userContent) or ("what" in userContent))):
        answer = "I am a virtual assistant created by the Faculty of Information Technology of Vietnam Aviation Academy, I have not been named."

    #Maps
    elif ((("area" in userContent) or ("location " in userContent) or ("position" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("counter" in userContent) or ("check-in" in userContent))):
        answer = "This is the airport check-in counter area, they will be shown on the map."
        #Gọi hàm bật map và show quầy thủ tục.
    elif (("bathroom" in userContent) or ("restroom" in userContent) or ("men's room" in userContent)):
        answer = "These are some of the toilets at the airport, they will be shown on the map."
        #Gọi hàm bật map và show nhà vệ sinh.
    elif ((("gate" in userContent) or ("door" in userContent) or ("exit" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and ("departure" in userContent)):
        answer = "These are some gates at the airport, they will be shown on the map."
        #Gọi hàm bật map và show toàn bộ cửa.
    elif ((("door" in userContent) or ("exit" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("emergency" in userContent) or ("exit" in userContent))):
        answer = "These are some of the exits from the airport, they will be shown on the map."
        #Gọi hàm bật map và show toàn bộ cửa ra ngoài.
    elif ((("area" in userContent) or ("location " in userContent) or ("position" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("customs" in userContent) or ("exit check-in" in userContent) or ("exit procedures" in userContent))):
        answer = "This is the customs area at the airport, they will be shown on the map."
        #Gọi hàm bật map và show khu vực hải quan.
    elif ((("area" in userContent) or ("location " in userContent) or ("position" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("medical" in userContent) or ("health care" in userContent) or ("ambulance" in userContent) or ("injury" in userContent) or ("patients" in userContent) or ("disease" in userContent))):
        answer = "This is the medical area at the airport, they will be shown on the map."
        #Gọi hàm bật map và show khu vực y tế.
    elif (("stairs" in userContent) or ("staircase" in userContent) or ("elevator" in userContent) or ("escalator" in userContent)):
        answer = "These are some of the stairs and elevators at the airport, they will be shown on the map."
        #Gọi hàm bật map và show thang.
    elif ((("area" in userContent) or ("location " in userContent) or ("position" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("restaurant" in userContent) or ("store" in userContent) or ("shop" in userContent) or ("reigser" in userContent) or ("counter" in userContent) or ("dining bar" in userContent)
                or ("food" in userContent) or ("nutrition" in userContent) or ("food-stuff" in userContent) or ("drinking" in userContent) or ("drink" in userContent))):
        answer = "This is the restaurant and convenience store area at the airport, they will be shown on the map."
        #Gọi hàm bật map và show nhà hàng.
    elif ((("area" in userContent) or ("location " in userContent) or ("position" in userContent) or ("where" in userContent) or ("which way" in userContent)) 
          and (("airline" in userContent) or ("airlines" in userContent))):
        answer = "This is the area of some airlines at the airport, they will be shown on the map."
        #Gọi hàm bật map và show hãng hàng không.

    #Flight
    elif ((("information" in userContent) or ("schedule" in userContent) or ("calendar" in userContent) or ("time" in userContent) or ("flight" in userContent))     
          and (("my" in userContent) or ("me" in userContent))):
        answer = "Please go to the nearest service desk for details."



    #################
    #chưa set tiếng anh
    elif ((("information" in userContent) or ("schedule" in userContent) or ("calendar" in userContent) or ("time" in userContent) or ("flight" in userContent))     
        and (("hôm nay" in userContent) or ("hiện tại" in userContent) or ("bây giờ" in userContent))):
        #Kiểm tra lịch bay == ngày && >= giờ
        #if  còn chuyến 
        answer = "Here's a list of available flights."
        #else
        #answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
    elif ((("thông tin" in userContent) or ("lịch" in userContent) or ("thời gian" in userContent) or ("chuyến" in userContent))     
          and ("bay" in userContent) and (("điểm đáp" in userContent) or ("đến" in userContent))):
        city = ["bình định", "bình dương"]
        temp = False
        #từ chuỗi check lại
        for i in city:
            if i in userContent:
                city = i
                #kiểm tra trong danh sách
                
        #if  còn chuyến 
        answer = "Here's a list of available flights."
        #else
        #answer = "Hiện tại cảng hàng không đã hết chuyến bay quý khách cần tìm, quý khách vui lòng chọn lại."
    
    #set thêm một số tính năng hỏi hãng, giá
    ###############
    elif (((("information" in userContent) or ("calendar" in userContent) or ("time" in userContent)) 
           and ("flight" in userContent)) 
           or ("flight" in userContent)) or ("schedule" in userContent):
        answer = "Here's a list of available flights."
        #Gọi hàm bật lịch bay

        

    #GPT Service
    else:
        answer = gptService(userContent)

    return answer
