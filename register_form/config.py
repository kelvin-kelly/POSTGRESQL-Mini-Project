conf={
    'dbname':'postgres',
    'user':'postgres.yidrwyfuuibnutiiocge',
    'password':'SUPABASEsupabase',
    'host':'aws-0-eu-central-1.pooler.supabase.com',
    'port':'6543'
}

class Config:
    SQLALCHEMY_DATABASE_URI=f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}:5432/postgres"