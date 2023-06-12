def example(currdate,q):
    n=len(currdate)
    mm=int(currdate[n-2:])
    y=int(currdate[:n-2])
    if (mm<10):
        if(mm!=1):
            prev_date=currdate[:n-2]+"0"+str(mm-1)
            future_date=str(y+1)+"0"+str(mm-1)
        else:
            prev_month=str(y-1)+"12"
            future_date=str(y)+"12"
    else:
        prev_month=currdate[:n-2]+str(mm-1)
        future_date=str(y+1)+str(mm-1)
        
    if (q==1):
        prev_quater="Q"+str(q+3)+"_"+str(y-1)
    else:
        prev_quater="Q"+str(q-1)+"_"+str(y+1)
#     future_date=str(y+1)+"0"+str(mm-1)
    if (q==4):
        
        future_quater="Q"+str(q-3)+"_"+str(y+1)
    else:
        future_quater="Q"+str(q+1)+"_"+str(y)

    dict1=dict({'prev_date':prev_month,'prev_quater':prev_quater,'future_date':future_date,'future_quater':future_quater})
    return dict1
def main():
    curr_date=input()
    quater=int(input())
    print(example(curr_date,quater))
    if _name_ == "_main_":
      main()
