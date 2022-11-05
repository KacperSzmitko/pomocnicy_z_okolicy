import type { PayloadAction } from "@reduxjs/toolkit";
import { createSlice } from "@reduxjs/toolkit";

export interface ReportType {
  type_name: string;
  lifespan: number;
}

export interface Report {
  id?: number;
  notified?: boolean;
  latitude: number;
  altitude: number;
  report_type: string;
  report_state: string;
  time?: string;
  max_people?: number;
  current_people?: number;
  description?: string;
}

export interface ReportsType {
  current_latitude: number;
  current_altitude: number;
  reports: Report[];
  avaliable_report_types: ReportType[];
  avaliable_report_states: string[];
}

const initialState: ReportsType = {
  current_latitude: 52.40,
  current_altitude: 16.91,
  reports: [],
  avaliable_report_types: [],
  avaliable_report_states: [],
};

const reportsSlice = createSlice({
  name: "reports",
  initialState,
  reducers: {
    reportCreated(state: ReportsType, action: PayloadAction<Report>) {
      state.reports.push(action.payload);
    },
    reportsFetched(state: ReportsType, action: PayloadAction<Report[]>) {
      if (state.reports.length > 0) {
      const index = action.payload.findIndex(
        (r) => r.id === state.reports.at(-1)!.id
      );
      if (index === -1) {
        const newReports = action.payload.slice(index, action.payload.length);
        state.reports.concat(
          newReports.map((r) => ({ ...r, notified: false }))
        );
      }
    }
    else state.reports = action.payload.map((r) => ({ ...r, notified: false }));
    },
    reportAccepted(state: ReportsType, action: PayloadAction<number>) {},
    reportTypesFetched(
      state: ReportsType,
      action: PayloadAction<ReportType[]>
    ) {
      state.avaliable_report_types = action.payload;
    },
    reportStatesFetched(
      state: ReportsType,
      action: PayloadAction<string[]>
    ) {
      state.avaliable_report_states = action.payload;
    },
    reportNotified(state: ReportsType, action: PayloadAction<number[]>) {
        state.reports.forEach((r) => {
            if (action.payload.includes(r.id!)) {
            r.notified = true;
            }
        });
    },
  },
});

export const {
  reportCreated,
  reportsFetched,
  reportAccepted,
  reportTypesFetched,
  reportStatesFetched
} = reportsSlice.actions;
export default reportsSlice.reducer;
