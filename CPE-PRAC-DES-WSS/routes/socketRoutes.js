import express from 'express';
import expressWsPkg from 'express-ws';

const router = express.Router();
const expressWs = expressWsPkg(router);

router.ws('/readings', (ws, req) => {
  ws.on('message', (msg) => {
    console.log(msg);
    // ws.send(msg);
  });
});

export default router;
