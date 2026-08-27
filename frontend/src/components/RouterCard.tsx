interface RouterCardProps {
    router: {
        hostname: string;
        model: string;
        board: string;
        firmware: string;
        kernel: string;
    };
}

function RouterCard({ router }: RouterCardProps) {
    return (
        <div className="dashboard-card">
            <h2>Router Information</h2>

            <div className="info-row">
                <span>Hostname</span>
                <strong>{router.hostname}</strong>
            </div>

            <div className="info-row">
                <span>Model</span>
                <strong>{router.model}</strong>
            </div>

            <div className="info-row">
                <span>Board</span>
                <strong>{router.board}</strong>
            </div>

            <div className="info-row">
                <span>Firmware</span>
                <strong>{router.firmware}</strong>
            </div>

            <div className="info-row">
                <span>Kernel</span>
                <strong>{router.kernel}</strong>
            </div>
        </div>
    );
}

export default RouterCard;