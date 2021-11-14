start_index = 1
my_step = 1

while True:
    try:
        for index in range(start_index,len(check_this_data_mass)):

            kwak = np.array([[0,0,0]]*44)
            counter = 0
            for i in range(0,44):
                for j in range(0,3):
                    kwak[i][j] = check_this_data_mass[counter]
                    counter+=1

            df = pd.DataFrame(kwak, columns = ['1','2','3'])
            df.index += 1
            df = df.T
            data_store = df
            #print(data_store.T)
            all_cost = 0 
            grouped = np.unique(data_check.CHEQUEID)

            for i in grouped.tolist():
                mydata = data_check[data_check.CHEQUEID == i]
                arr = mydata.LAGERID.tolist()
                arr = [get_number_of_position_shelf2(ik,data_store) for ik in arr]

                ultra_ans = simple_path_to_44(arr)[1]
                mydata = mydata.reset_index()
                #print(mydata)
                for i in range(0,len(mydata)):
                    mydata.KOLVO[i] = get_number_of_position_shelf(mydata.LAGERID[i],data_store)*mydata.KOLVO[i]

                ultra_ans += sum(mydata.KOLVO)
                #print('ultra answer:')
                #print(ultra_ans)

                all_cost += ultra_ans
                #print('ans ',str(all_cost))

            #print(all_cost)
            old_cost = all_cost


            check_this_data_mass = replace_44(index,my_step,check_this_data_mass)
            kwak = np.array([[0,0,0]]*44)
            counter = 0
            for i in range(0,44):
                for j in range(0,3):
                    kwak[i][j] = check_this_data_mass[counter]
                    counter+=1

            df = pd.DataFrame(kwak, columns = ['1','2','3'])
            df.index += 1
            df = df.T
            data_store = df
            #print(data_store.T)
            all_cost = 0 
            grouped = np.unique(data_check.CHEQUEID)

            for i in grouped.tolist():
                mydata = data_check[data_check.CHEQUEID == i]
                arr = mydata.LAGERID.tolist()
                arr = [get_number_of_position_shelf2(ik,data_store) for ik in arr]

                ultra_ans = simple_path_to_44(arr)[1]
                mydata = mydata.reset_index()
                #print(mydata)
                for i in range(0,len(mydata)):
                    mydata.KOLVO[i] = get_number_of_position_shelf(mydata.LAGERID[i],data_store)*mydata.KOLVO[i]

                ultra_ans += sum(mydata.KOLVO)
                #print('ultra answer:')
                #print(ultra_ans)

                all_cost += ultra_ans
                #print('ans ',str(all_cost))

            new_cost = all_cost

            if new_cost > old_cost:
                check_this_data_mass = replace_44(index,my_step,check_this_data_mass)

            print(min(new_cost,old_cost))
            print(check_this_data_mass)
            text_file = open(str(all_cost)+".txt", "w")
            text_file.write(str(check_this_data_mass))
    except:
        start_index = 0
        my_step += 1