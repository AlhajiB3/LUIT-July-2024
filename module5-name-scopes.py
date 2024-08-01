def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var='Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

def show_truth():
    global mysterious_var
    mysterious_var.append('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)