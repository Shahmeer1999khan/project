
const socket = new WebSocket('ws://http://127.0.0.1:8000/ws/hello/');

socket.onopen = (event) => {
    console.log('WebSocket connection opened:', event);
    socket.send(JSON.stringify({ message: 'Hello, server!' }));
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log('Message from server:', data.message);
};

socket.onclose = (event) => {
    console.log('WebSocket connection closed:', event);
};
