import React from 'react';
import { Routes, Route } from "react-router-dom";
import HomePage from "../common/HomePage";
import LoginPage from "../features/auth/LoginPage";
import Notifications from '../features/responseReport/Notifications';

function App() {
  return (
    <div className="app" id="main_window">
      <Routes>
        <Route path="/" element={<HomePage />}>
          <Route path="/notifications" element={<Notifications />}></Route>
          <Route path="*" element={<div></div>}></Route>
        </Route>
        <Route path="login" element={<LoginPage />}></Route>
        <Route path="send_report" element={<div></div>}></Route>
      </Routes>
    </div>
  );
}

export default App;
/*{
              "report_state":"STATE1",
              "id":123,
              "notified":false,
              "latitude":52,
              "altitude":17,
              "report_type":{"type_name":"DANGER", "lifespan":5},
              "time":'01 Jan 2022 00:00:00 GMT',
              "max_people":5,
              "current_people": 0,
              "description": "Niebezpieczny rój os atakuje"} */
