import React from 'react'
import Map from '../map/Map';
import ReportType from '../reportType/reportType'
import {Report} from '../reports/reportsSlice'
import ReportTrackDecission from '../reportTrackDecission/reportTrackDecission'
import ReportInfo from '../reportInfo/reportInfo'


function TrackReport(report:Report) {
    return <div className="response-report">
                <div className="report-type">
                    {report.report_type.type_name}
                </div>
                <div className="map">
                    <Map lat={report.latitude} lan={report.altitude}/>
                </div>
                <div className="report-info">
                    <div className='report-info-description'>
                        {report.description}
                    </div>
                    <div className='report-info-bottom'>
                        <div className='report-info-bottom-left'>
                            <div className='report-info-distance'>
                                //TODO current distance to the report location
                            </div>
                            <div className='report-info-time'>
                                //TODO time passed from report submission in minutes
                            </div>
                        </div>
                        <div className='report-info-bottom-right report-info-user'>
                            <div></div>
                        </div>

                    </div>
                </div>
                <div className="response-react">
                    <div>
                        <button className="deny-button">DENY</button> 
                        <div className="accepted-button-residue">ACCEPTED</button>
                    </div>
                </div>
            </div>;
}

export default React.memo(TrackReport);