import React from 'react'
import Map from '../map/Map';
import ReportType from '../reportType/reportType'
import {Report} from '../reports/reportsSlice'
import ReportTrackDecission from '../reportTrackDecission/reportTrackDecission'
import ReportInfo from '../reportInfo/reportInfo'


function TrackReport(report:Report) {
    return <div className="response-report">
                <div className="report-type">
                    <ReportType reportType={report.report_type.type_name} />
                </div>
                <div className="map">
                    <Map />
                </div>
                <div className="report-info">
                    <ReportInfo report={report}/>
                </div>
                <div className="response-react">
                    <ReportTrackDecission />
                </div>
            </div>;
}

export default React.memo(TrackReport);