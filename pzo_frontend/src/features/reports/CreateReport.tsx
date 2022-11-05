import React, {useState} from 'react'
import { useAppDispatch } from '../../common/hooks'

export default function SendReport() {
    const dispach = useAppDispatch();
    const [reportType, setReportType] = useState("Danger");
    const handleRadioChange =(e: any)=> {
        setReportType(e.target.value)
    }

    async function onSubmit (e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        //dispach(createReport(email, password));
    }

    return (
        <div>
            <form onSubmit={onSubmit}>
                <div>
                    <div>
                        <input type="radio" id="danger" name="reportType" value="DANGER"/>
                    </div>
                    <div>
                        <input type="radio" id="help" name="reportType" value="HELP"/>
                    </div>
                    <div>
                        <input type="radio" id="info" name="reportType" value="INFO"/>
                    </div>
                </div>
                <div>
                    <textarea id="description" name="description" maxLength={255}></textarea>
                </div>
                <div>
                    <input type="submit" value="Send report"/>
                </div>
            </form>
        </div>
    )
}