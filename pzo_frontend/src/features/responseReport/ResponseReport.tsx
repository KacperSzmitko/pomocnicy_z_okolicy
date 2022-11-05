import React from 'react'
import Map from '../map/Map';
import reportType from '../reportType/reportType'
import {Report} from '../reports/reportsSlice'
import reportResponseDecission from '../reportResponseDecission/reportResponseDecission'
import reportInfo from '../reportInfo/reportInfo'


function ResponseReport(report:Report) {
    return <div className="response-report">
                <div className="report-type">
                    <reportType reportType={report.report_type.type_name} />
                </div>
                <div className="map">
                    <Map />
                </div>
                <div className="report-info">
                    <reportInfo report={report} />
                </div>
                <div className="response-react">
                    <reportResponseDecission />
                </div>
            </div>;
}

export default React.memo(ResponseReport);