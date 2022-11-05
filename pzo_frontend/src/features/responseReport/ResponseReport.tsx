import { Data } from '@react-google-maps/api';
import React, { useEffect, useState } from 'react'
import { useAppDispatch, useAppSelector } from '../../common/hooks';
import Map from '../map/Map';
import { acceptReport } from '../reports/actions';
import {Report} from '../reports/reportsSlice'

export interface PropType {
    report: Report;
  }



function ResponseReport({report}: PropType) {
    const curr_lat =  useAppSelector((state) => state.reducer.reportsSlice.current_latitude)
    const curr_lon =  useAppSelector((state) => state.reducer.reportsSlice.current_altitude)
    const curr_distance = React.useMemo(()=>(Math.pow(Math.pow(curr_lat-report.latitude, 2) + Math.pow(curr_lon-report.altitude, 2), 0.5)/360)*6356752, [curr_lat, curr_lon])
    const d = new Date();
    let reportTimeSec = d.getSeconds();
    const [curr_time, settime] = useState(d.getSeconds());
    const dispach = useAppDispatch();
    useEffect(() => {
        setInterval(() => settime(Date.now()), 5000);
    }, []);
    let reportAcceptanceState="NONE"

    function reportDenied(){
        reportAcceptanceState = "DENIED"
    }

    function reportAccepted(){
        reportAcceptanceState = "ACCEPTED"
        if (report.id !== undefined) dispach(acceptReport(report.id))
    }

    return (<div className="response-report">
                <div className="report-type">
                    {report.report_type}
                </div>
                <div className="map">
                    <Map lat={report.latitude} lng={report.altitude}/>
                </div>
                <div className="report-info">
                    <div className='report-info-description'>
                        {report.description}
                    </div>
                    <div className='report-info-bottom'>
                        <div className='report-info-bottom-left'>
                            <div className='report-info-distance'>
                                {curr_distance}
                            </div>
                            <div className='report-info-time'>
                                {(curr_time - reportTimeSec)/1000}
                            </div>
                        </div>
                        <div className='report-info-bottom-right report-info-user'>
                            <div></div>
                        </div>

                    </div>
                </div>
                <div className="response-react">
                    {reportAcceptanceState === "NONE"} ?
                        <div>
                            {report.report_type === "HELP"} ?
                            {<div><button className="deny-button">DENY</button> <button onClick={reportAccepted} className="accept-button">ACCEPT</button> </div>} :
                            {<button className="ok-button">OK</button>}
                        </div> :
                            <div>
                                RESPONSE SENT
                            </div>
                </div>
            </div>)
}

export default React.memo(ResponseReport);
