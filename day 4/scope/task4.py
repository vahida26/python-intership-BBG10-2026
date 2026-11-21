def check_status():
    status="panding"
    def update():
        nonlocal status
        status = "completed"
    update()
    print("final status :",status)
check_status()