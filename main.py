from task_model import TaskModel

def main():
  task = TaskModel("Estudiar para el examen")
  print(f"Tarea creada: {task.get_task_name()}")
  task.mark_as_completed()
  print(f"Tarea completada: {task.is_task_completed()}")

if __name__ == "__main__":
  main()