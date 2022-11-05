import React, {useState} from 'react'
import { useAppDispatch, useAppSelector } from '../../common/hooks'
import { Report } from "./reportsSlice"
import { createReport } from "./actions"

export default function SendReport() {
    const dispach = useAppDispatch();
    const [reportType, setReportType] = useState("Danger");
    const [reportDescription, setReportDescription] = useState("");
    const currentLat = useAppSelector(state => state.reducer.reportsSlice.current_latitude)
    const currentLon = useAppSelector(state => state.reducer.reportsSlice.current_altitude)

    async function onSubmit (e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        dispach(createReport({
            report_type: reportType, 
            latitude: currentLat, 
            altitude: currentLon,
            description: reportDescription,
        }));
    }

    return (
        <div>
            <form onSubmit={onSubmit}>
                <div>
                    <div>
                        <input type="radio" id="danger" name="reportType" value="DANGER" 
                        onChange={e => setReportType(e.target.value)}/>
                    </div>
                    <div>
                        <input type="radio" id="help" name="reportType" value="HELP"
                        onChange={e => setReportType(e.target.value)}/>
                    </div>
                    <div>
                        <input type="radio" id="info" name="reportType" value="INFO"
                        onChange={e => setReportType(e.target.value)}/>
                    </div>
                </div>
                <div>
                    <textarea id="description" name="description" maxLength={255}
                    value={reportDescription} onChange={e => setReportDescription(e.target.value)}>
                    </textarea>
                </div>
                <div>
                    <input type="submit" value="Send report"/>
                </div>
            </form>
        </div>
    )
}