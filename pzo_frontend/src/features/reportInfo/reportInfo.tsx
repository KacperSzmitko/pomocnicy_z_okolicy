import React from 'react'
import {Report} from '../reports/reportsSlice'
import UserInfoView from '../userInfo/userInfoView'

function ReportInfo(report:Report) {
    return  <div>
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
                        <UserInfoView user = {???}/> //TODO get user form report
                    </div>
                    
                </div>
                

            </div>;
}

export default React.memo(ReportInfo);