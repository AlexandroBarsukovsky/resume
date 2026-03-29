-- database/init.sql
-- Инициализация базы данных для GTM-инфраструктуры Sourcegraph

-- Таблица аккаунтов (синхронизируется с Salesforce)
CREATE TABLE IF NOT EXISTS accounts (
    id VARCHAR(18) PRIMARY KEY,                     -- Salesforce ID
    name VARCHAR(255) NOT NULL,
    account_score NUMERIC(5,2) DEFAULT 0,           -- 0..1
    health_score NUMERIC(5,2) DEFAULT 0,            -- 0..1
    last_activity TIMESTAMP,
    risk_flag BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица возможностей (Opportunity)
CREATE TABLE IF NOT EXISTS opportunities (
    id VARCHAR(18) PRIMARY KEY,                     -- Salesforce ID
    account_id VARCHAR(18) NOT NULL REFERENCES accounts(id),
    stage VARCHAR(50) NOT NULL,
    win_probability NUMERIC(5,2) DEFAULT 0,         -- 0..1
    amount NUMERIC(15,2) NOT NULL,
    forecast_category VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица задач (Task)
CREATE TABLE IF NOT EXISTS tasks (
    id VARCHAR(50) PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
    description TEXT,
    assigned_to VARCHAR(255),
    related_to_id VARCHAR(18),                      -- account или opportunity ID
    status VARCHAR(20) DEFAULT 'pending',
    priority VARCHAR(10) DEFAULT 'normal',
    created_by_agent VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

-- Таблица истории Health Score
CREATE TABLE IF NOT EXISTS health_score_history (
    id SERIAL PRIMARY KEY,
    account_id VARCHAR(18) NOT NULL REFERENCES accounts(id),
    date DATE NOT NULL,
    health_score NUMERIC(5,2) NOT NULL,
    status VARCHAR(10) CHECK (status IN ('green', 'yellow', 'red')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица бюджета (опционально, для учёта рекламных расходов, комиссий и т.д.)
CREATE TABLE IF NOT EXISTS budget (
    article VARCHAR(50) PRIMARY KEY,
    limit_amount NUMERIC(10,2) NOT NULL CHECK (limit_amount >= 0),
    spent NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (spent >= 0),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица истории бюджета
CREATE TABLE IF NOT EXISTS budget_history (
    id SERIAL PRIMARY KEY,
    article VARCHAR(50) NOT NULL REFERENCES budget(article),
    amount NUMERIC(10,2) NOT NULL,
    reason TEXT,
    source_agent VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для ускорения запросов
CREATE INDEX idx_accounts_score ON accounts(account_score);
CREATE INDEX idx_accounts_health ON accounts(health_score);
CREATE INDEX idx_opportunities_account ON opportunities(account_id);
CREATE INDEX idx_opportunities_stage ON opportunities(stage);
CREATE INDEX idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_health_score_account_date ON health_score_history(account_id, date);

-- Начальные данные: бюджет (можно оставить пустым или добавить значения по умолчанию)
INSERT INTO budget (article, limit_amount) VALUES
('advertising', 150000),
('marketing', 100000)
ON CONFLICT (article) DO NOTHING;