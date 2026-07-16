from src.core.application import AthenaApplication


print("=" * 60)
print("ATHENA CORE")
print("=" * 60)


app = AthenaApplication()


try:

    app.boot()


except KeyboardInterrupt:

    app.shutdown()
