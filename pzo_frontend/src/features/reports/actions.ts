import axios from "axios";
import { BASE_API_URL } from "../../common/constans";
import {
  Report,
  reportCreated,
  reportsFetched,
  reportAccepted,
  reportTypesFetched,
} from "./reportsSlice";
import { Dispatch } from "redux";

export const createReport = (report: Report) => (dispach: Dispatch) => {
  axios
    .post(BASE_API_URL + "app/report/", report)
    .then((response) => {
      dispach(reportCreated(response.data));
    })
    .catch((err) => console.log(err));
};

export const getReports =
  (latitude: number, altitude: number) => (dispach: Dispatch) => {
    axios
      .get(BASE_API_URL + "app/report/", { params: { latitude, altitude } })
      .then((response) => {
        dispach(reportsFetched(response.data));
      })
      .catch((err) => console.log(err));
  };

export const acceptReport = (reportId: number) => (dispach: Dispatch) => {
  axios
    .get(BASE_API_URL + `app/accept_report/${reportId}`)
    .then((response) => {
      dispach(reportAccepted(reportId));
    })
    .catch((err) => console.log(err));
};

export const getReportTypes = () => (dispach: Dispatch) => {
  axios
    .get(BASE_API_URL + "app/report/types/")
    .then((response) => {
      dispach(reportTypesFetched(response.data));
    })
    .catch((err) => console.log(err));
};
