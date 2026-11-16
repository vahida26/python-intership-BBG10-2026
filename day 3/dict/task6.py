emp_name={"John":50000,
          "Alice":60000,
          "Bob":55000,
          "Eve":70000,
          "Charlie":65000
          }
sorted_emp_name=sorted(emp_name.items(),
                       key=lambda x:x[1],reverse=True)
top3=sorted_emp_name[:3]
print(top3)