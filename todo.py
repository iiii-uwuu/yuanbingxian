import json
import os

TASKS_FILE="tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE,"r",encoding="utf-8")as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE,"w",encoding="utf-8")as f:
        json.dump(tasks,f,ensure_ascii=False,indent=2)

def show_tasks(tasks):
    if not tasks:
        print("✨ 暂无任务，快去添加吧！")
        return
    for task in tasks:
        status="✅"if task["done"] else "⏳"
        print(f"{status}[{task['id']}]{task['name']}")

def add_task(tasks,name):
    new_id=max([t['id'] for t in tasks],default=0)+1
    tasks.append({"id":new_id,"name":name,"done":False})
    save_tasks(tasks)
    print(f"✔ 已添加任务：{name}")

def complete_task(tasks,task_id):
    for task in tasks:
        if task['id']==task_id:
            task['done']=True
            save_tasks(tasks)
            print(f"🎉 完成任务：{task['name']}")
            return
    print("❌ 未找到该编号的任务")

def delete_task(tasks,task_id):
    pre=0
    for task in tasks:
        pre+=1
        if task["id"]==task_id:
            tasks.pop(pre-1)
            save_tasks(tasks)
            return
    print("❌ 未找到该编号的任务")
    
def main():
    tasks=load_tasks()
    print("📋 终端待办工具 (输入 help 查看命令)")
    while True:
        cmd=input(">").strip()
        if cmd=="list":
            show_tasks(tasks)
        elif cmd.startswith("add"):
            name=cmd[4:].strip()
            if name:
                add_task(tasks,name)
            else:
                print("请填写任务内容")
        elif cmd.startswith("done "):
            try:
                task_id=int(cmd[5:].strip())
                complete_task(tasks,task_id)
            except ValueError:
                print("请输入正确的任务编号")
        elif cmd=="help":
            print("可用命令：list, add <任务名>, done <编号>, exit")
        elif cmd.startswith("delete "):
            try:
                task_id=int(cmd[7:].strip())
                delete_task(tasks,task_id)
            except ValueError:
                print("请输入正确的任务编号")
        elif cmd=="exit":
            print("👋 再见！")
            break
        else:
            print("未知命令，输入 help 查看帮助")

if __name__ =="__main__":
    main()



