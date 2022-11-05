import { combineReducers } from "redux";
import userInfoSlice from "../features/userInfo/userInfoSlice";
import reportsSlice from "../features/reports/reportsSlice";

export default combineReducers({
  userInfoSlice,
  reportsSlice,
});
