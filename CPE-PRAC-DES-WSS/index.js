import express from 'express';
import dotenv from 'dotenv';
import expressWsPkg from 'express-ws';
import router from './routes/socketRoutes.js';

dotenv.config();
const port = process.env.PORT;

const app = express();
const expressWs = expressWsPkg(app);

app.use("/", router);

app.listen(port, () => {
  console.log(`WebSocket server is running on port ${ port }`);
});