from celery import shared_task

@shared_task
def test_func():
    try:
        for i in range(10):
            print(i)
        print("Task executed successfully!")
        return {'status': 'Task executed successfully!'}
    except Exception as e:
        print(f"Task execution failed: {e}")
        return {'status': 'Task execution failed'}