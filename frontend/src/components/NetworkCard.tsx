interface NetworkCardProps {
    network: Record<string, any>;
}

function NetworkCard({ network }: NetworkCardProps) {
    return (
        <div className="dashboard-card">
            <h2>Network Interfaces</h2>

            {Object.entries(network).map(([name, device]) => (
                <div className="network-interface" key={name}>
                    <div className="interface-header">
                        <strong>{name}</strong>

                        <span className={device.up ? "status-up" : "status-down"}>
                            {device.up ? "UP" : "DOWN"}
                        </span>
                    </div>

                    <div className="info-row">
                        <span>Type</span>
                        <strong>{device.devtype}</strong>
                    </div>

                    <div className="info-row">
                        <span>MAC</span>
                        <strong>{device.mac}</strong>
                    </div>

                    <div className="info-row">
                        <span>MTU</span>
                        <strong>{device.mtu}</strong>
                    </div>

                    {device.ipaddrs?.length > 0 && (
                        <div className="info-row">
                            <span>IPv4</span>
                            <strong>{device.ipaddrs[0].address}</strong>
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
}

export default NetworkCard;