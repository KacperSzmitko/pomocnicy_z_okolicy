import React from 'react'
import Map from '../map/Map';
import ReportType from '../reportType/reportType'
import {Report} from '../reports/reportsSlice'
import reportTrackDecission from '../reportTrackDecission/reportTrackDecission'
import reportInfo from '../reportInfo/reportInfo'

function TrackReport(report:Report) {
    return <div className="response-report">
                <div className="report-type">
                    <ReportType type={report.report_type.type_name} />
                </div>
                <div className="map">
                    <Map />
                </div>
                <div className="report-info">
                    <reportInfo report={report}/>
                </div>
                <div className="response-react">
                    <reportTrackDecission />
                </div>
            </div>;
}

export default React.memo(ResponseReport);