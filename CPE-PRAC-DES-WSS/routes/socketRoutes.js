import express from 'express';
import expressWsPkg from 'express-ws';

const router = express.Router();
const expressWs = expressWsPkg(router);

// Store all connected frontend clients
const connectedClients = new Set();

// Route for receiving sensors data from esp32 -- working
router.ws('/readings', (ws, req) => {
  ws.on('message', (msg) => {
    console.log(msg);
    // ws.send(msg);

    // Broadcast the received message to all connected frontend clients
    connectedClients.forEach(client => {
      if (client.readyState === 1) { // 1 = OPEN state
        client.send(msg);
      }
    });
  });

  ws.on('close', () => {
    console.log('ESP32 connection closed');
  });
});

// Route for sending sensors data to frontend
router.ws('/datas', (ws, req) => {
  // Add new frontend connection to the set
  connectedClients.add(ws);

  ws.on('close', () => {
    connectedClients.delete(ws);
    console.log('Frontend disconnected');
  });

  console.log('Frontend connected');
});

export default router;
