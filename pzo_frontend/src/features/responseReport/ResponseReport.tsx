import React from 'react'
import Map from '../map/Map';
import ReportType from '../reportType/reportType'
import {Report} from '../reports/reportsSlice'
import ReportResponseDecission from '../reportResponseDecission/reportResponseDecission'
import ReportInfo from '../reportInfo/reportInfo'


function ResponseReport(report:Report) {
    return <div className="response-report">
                <div className="report-type">
                    <ReportType reportType={report.report_type.type_name} />
                </div>
                <div className="map">
                    <Map />
                </div>
                <div className="report-info">
                    <ReportInfo report={report} />
                </div>
                <div className="response-react">
                    <ReportResponseDecission />
                </div>
            </div>;
}

export default React.memo(ResponseReport);