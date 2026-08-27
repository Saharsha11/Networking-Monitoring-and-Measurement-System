interface DhcpCardProps {
    dhcp: {
        dhcp_leases: any[];
        dhcp6_leases: any[];
    };
}

function DhcpCard({ dhcp }: DhcpCardProps) {
    const leases = dhcp.dhcp_leases || [];

    return (
        <div className="dashboard-card">
            <div className="card-header">
                <h2>DHCP Clients</h2>
                <span className="client-count">
                    {leases.length} Clients
                </span>
            </div>

            {leases.length === 0 ? (
                <p className="empty-state">
                    No DHCP clients connected
                </p>
            ) : (
                <div className="dhcp-table">
                    <div className="dhcp-row dhcp-header">
                        <span>Hostname</span>
                        <span>IP Address</span>
                        <span>MAC Address</span>
                    </div>

                    {leases.map((lease, index) => (
                        <div className="dhcp-row" key={index}>
                            <span>{lease.hostname || "Unknown"}</span>
                            <span>{lease.ipaddr || "-"}</span>
                            <span>{lease.macaddr || "-"}</span>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default DhcpCard;