# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        message = json.loads(text_data)
        event_type = message.get('type')

        if event_type == 'update_employee':
            employee_id = message.get('employee_id')
            await self.handle_update_employee(employee_id)
        elif event_type == 'delete_employee':
            employee_id = message.get('employee_id')
            await self.handle_delete_employee(employee_id)
            
        else:
            pass
            

    async def handle_update_employee(self, employee_id):
        await self.send(text_data=json.dumps({'event': 'employee_updated', 'employee_id': employee_id}))

    async def handle_delete_employee(self, employee_id):
        await self.send(text_data=json.dumps({'event': 'employee_deleted', 'employee_id':employee_id}))