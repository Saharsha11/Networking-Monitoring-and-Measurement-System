interface WirelessCardProps {
    wireless: Record<string, any>;
}

function WirelessCard({ wireless }: WirelessCardProps) {
    return (
        <div className="dashboard-card">
            <h2>Wireless</h2>

            {Object.entries(wireless).map(([radioName, radio]) => (
                <div className="wireless-radio" key={radioName}>
                    <div className="interface-header">
                        <strong>{radioName}</strong>

                        <span
                            className={
                                radio.up ? "status-up" : "status-down"
                            }
                        >
                            {radio.up ? "UP" : "DOWN"}
                        </span>
                    </div>

                    <div className="info-row">
                        <span>Band</span>
                        <strong>{radio.band}</strong>
                    </div>

                    <div className="info-row">
                        <span>Channel</span>
                        <strong>{radio.channel}</strong>
                    </div>

                    <div className="info-row">
                        <span>HT Mode</span>
                        <strong>{radio.htmode}</strong>
                    </div>

                    <div className="info-row">
                        <span>Country</span>
                        <strong>{radio.country}</strong>
                    </div>

                    {radio.interfaces?.map(
                        (wifiInterface: any, index: number) => (
                            <div key={index}>
                                <div className="info-row">
                                    <span>SSID</span>
                                    <strong>
                                        {wifiInterface.ssid || "N/A"}
                                    </strong>
                                </div>

                                <div className="info-row">
                                    <span>Mode</span>
                                    <strong>
                                        {wifiInterface.mode || "N/A"}
                                    </strong>
                                </div>

                                <div className="info-row">
                                    <span>Encryption</span>
                                    <strong>
                                        {wifiInterface.encryption ||
                                            "N/A"}
                                    </strong>
                                </div>
                            </div>
                        )
                    )}
                </div>
            ))}
        </div>
    );
}

export default WirelessCard;