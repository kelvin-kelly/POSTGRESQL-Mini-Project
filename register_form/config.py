db_config={
    'dbname':'postgres',
    'user':'postgres.yidrwyfuuibnutiiocge',
    'password':'SUPABASEsupabase',
    'host':'aws-0-eu-central-1.pooler.supabase.com',
    'port':'6543'
}

app.config["SQLALCHEMY_DATABASE_URI"]=f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:6543/postgres"

