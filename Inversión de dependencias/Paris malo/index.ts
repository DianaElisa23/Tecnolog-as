class Paris2024Provider {
    top(n) {
        
        const data = [
            {rank: 1, country: "usa", gold: 40, silver: 44, bronze: 42},
            {rank: 1, country: "chn", gold: 40, silver: 44, bronze: 42},
            {rank: 1, country: "jpn", gold: 25, silver: 44, bronze: 42},
            {rank: 1, country: "fra", gold: 16, silver: 44, bronze: 42},
            {rank: 1, country: "aus", gold: 18, silver: 44, bronze: 42},
        ];
        return data.slice(0, n);
    }
}

class MedalService {
    private provider: Paris2024Provider;

    constructor() {
        this.provider = new Paris2024Provider();
    }

    showTop(n) {
        const rows = this.provider.top(n);

        console.log("\n === Paris 2024 ===");
        console.table(rows);
    }
}

const medallero = new MedalService();
medallero.showTop(3);
