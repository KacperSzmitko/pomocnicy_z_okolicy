import React from 'react'

export default function SendReport() {
    return (
        <div>
            <form>
                <div>
                    <div>
                        <input type="radio" id="danger" name="reportType"/>
                    </div>
                    <div>
                        <input type="radio" id="help" name="reportType"/>
                    </div>
                    <div>
                        <input type="radio" id="info" name="reportType"/>
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