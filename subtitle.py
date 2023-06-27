
hours = input('Enter the hours : ')
minute = input('Enter the minute : ')
second = input('Enter the second : ')

TIME = hours + ":" + minute + ":" + second
print(TIME)
# TIME = '00:30:25'
text_for_write = []

en_file_name = 'D:\downloads\shrinking\program\Shrinking-S01-Complete\Shrinking S01 - Complete\English\Shrinking S01 - E01\Shrinking.S01E01_EngCP.srt'
en_file_name = "D:\downloads\shrinking\program\Shrinking-S01-Complete\Shrinking S01 - Complete\English\Shrinking S01 - E02\Shrinking.S01E02_EngCP.srt"
# en_file_name = 'Ted Lasso S01 - Complete/English/Ted Lasso S01 - E01/Ted Lasso - S01E01 WEB.eng.srt'
with open(en_file_name) as f:
    
    file = f.readlines()
    found_time = []
    for i in file:
        if i == "\n":
            continue
        x = i.strip()
        # print(x)
        # print('----------------------------------------------')
        dic = {}
        if x.startswith('0'):
        #    print(x)
           time = x.split()
           start = time[0][:8]
           end = time[-1][:8]
           
           dic['start'] = start
           dic['end'] = end
        #    print(time)
        time_input = TIME
        split_time = time_input.split(':')
        # print(split_time)
        # print(dic)
        
        if dic != {}:
            start = dic['start'].split(':')
            end = dic['end'].split(':')
            # print(start)
            
            
        
            # print(dic)
            # print('time 2 :'+ split_time[2])
            # print('start 2 :'+ start[2])
            # print('end 2 :'+ end[2])
            if int(split_time[1]) >= int(start[1]) and int(split_time[1]) <= int(end[1]):
                # print(start, '----', end)
                # print('--------------------------')
                if int(split_time[2]) >= int(start[2]) and int(split_time[2]) <= int(end[2]):
                    # print(start, '----', end)
                    # print('===========================================')
                    found_time.append(x)
                    text_for_write.append(x)
                    
    # print(found_time[0])
    # print(found_time)
    index = []
    for i in range(len(file)):
        line = file[i]
        if line.startswith(found_time[0]):
            index.append(i+1)
    
    if file[index[0]+2] != "\n" and not int(file[index[0]+2]) :       
        text_for_write.append(file[index[0]].strip())
        text_for_write.append(file[index[0]+1].strip())
        text_for_write.append(file[index[0]+2].strip())
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
            f.write('time : '+ text_for_write[0]+'\r\n'+ 'English : '+ text_for_write[1]+'\n'+ text_for_write[2] + '\n' + text_for_write[3] + '\r\n')
        
    elif file[index[0]+1] != "\n":
        text_for_write.append(file[index[0]].strip())
        text_for_write.append(file[index[0]+1].strip())
        
        
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
            f.write('time : '+ text_for_write[0]+'\r\n'+ 'English : '+ text_for_write[1]+'\n'+ text_for_write[2] + '\r\n')
        
    else:
        text_for_write.append(file[index[0]].strip())
        
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
            f.write('time : '+ text_for_write[0]+'\r\n'+ 'English : '+ text_for_write[1]+'\r\n')
        
            
    
fa_file_name = 'D:\downloads\shrinking\program\Shrinking-S01-Complete\Shrinking S01 - Complete\Persian\Shrinking S01 - E01\Shrinking.S01E01_EngCP[fa].srt'
fa_file_name = 'D:\downloads\shrinking\program\Shrinking-S01-Complete\Shrinking S01 - Complete\Persian\Shrinking S01 - E02\Shrinking.S01E02_EngCP[fa].srt'
# fa_file_name = 'D:\downloads\shrinking\program\Ted Lasso S01 - Complete\Persian\Ted Lasso S01 - E01\Ted Lasso - 01x01 - Pilot[FA].srt'


with open(fa_file_name, encoding='utf8') as f:
    print('in try')
    try:
        file = f.readlines()
        print('after try')
    except :
    
        with open(fa_file_name, encoding='utf16') as f:
            file = f.readlines()
    
    found_time = []
    print('now')
    for i in file:
        if i == "\n":
            continue
        x = i.strip()
        # print(x)
        # print('----------------------------------------------')
        dic = {}
        if x.startswith('0'):
        #    print(x)
           time = x.split()
           start = time[0][:8]
           end = time[-1][:8]
           
           dic['start'] = start
           dic['end'] = end
           
        time_input = TIME
        split_time = time_input.split(':')
        # print(dic)
        
        if dic != {}:
            start_time = dic['start'].split(':')
            end_time = dic['end'].split(':')
            # print(start)
            
            
            # print('split_time ', split_time)
            # print(dic)
            # print('second :'+ split_time[2])
            # print('start 2 :'+ start_time[2])
            # print('end 2 :'+ end_time[2])
            if int(split_time[1]) >= int(start_time[1]) and int(split_time[1]) <= int(end_time[1]):
                # print(x)
                # print('--------------------------')
                if int(split_time[2]) >= int(start_time[2]) and int(split_time[2]) <= int(end_time[2]):
                    # print(x)
                    # print('===========================================')
                    found_time.append(x)
           
    print(found_time[0])
    index = []
    for i in range(len(file)):
        line = file[i]
        if line.startswith(found_time[0]):
            index.append(i+1)
    if file[index[0]+2] != "\n" and not int(file[index[0]+2]):       
        text_for_write.append(file[index[0]].strip())
        text_for_write.append(file[index[0]+1].strip())
        text_for_write.append(file[index[0]+2].strip())
        print(text_for_write)
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
            f.write('translate : '+ text_for_write[-3] + '\n' + text_for_write[-2] + '\n' + text_for_write[-1] +'\r\n\r\n')
    
    elif file[index[0]+1] != "\n":
        text_for_write.append(file[index[0]].strip())
        text_for_write.append(file[index[0]+1].strip())
        print(text_for_write)
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
    
            f.write('translate : '+ text_for_write[-2] + '\n' + text_for_write[-1] +'\r\n\r\n')
    
    else:
        text_for_write.append(file[index[0]].strip())
        print(text_for_write)
        with open('learn_E1.txt', 'a', encoding='utf8') as f:
    
            f.write('translate : '+ text_for_write[-1] +'\r\n\r\n')
            
