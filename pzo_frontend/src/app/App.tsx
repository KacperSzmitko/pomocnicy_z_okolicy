import React from 'react';
import { Routes, Route } from "react-router-dom";
import HomePage from "../common/HomePage";
import LoginPage from "../features/auth/LoginPage";
import CreateReport from '../features/reports/CreateReport';
import Map from '../features/map/Map';

function App() {
  return (
    <div className="app" id="main_window">
      <Routes>
        <Route path="/" element={<HomePage />}>
          <Route path="/" element={<Map lat={52} lng={17} />}></Route>
          <Route path="*" element={<div></div>}></Route>
        </Route>
        <Route path="login" element={<LoginPage />}></Route>
        <Route path="create_report" element={<CreateReport />}></Route>
      </Routes>
    </div>
  );
}

export default App;
